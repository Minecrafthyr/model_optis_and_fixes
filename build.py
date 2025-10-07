import shutil
import json
import logging
import sys
import time
import os
import argparse
import zipfile
import io

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Thread
from os import path as op
from datetime import datetime as dt
from dataclasses import dataclass, replace
from zipfile import ZipFile
from typing import IO, Any, Iterable
from json.encoder import JSONEncoder
from contextlib import contextmanager

import jsonpatch
from PIL import Image

type AnyDict = dict[str, Any]
type BytesDict = dict[str, bytes]

logger = logging.getLogger()
release: bool = False


@dataclass(frozen=True)
class Config:
    """A config entry"""

    name: str
    src_dir: Path
    out_dir: Path
    extra_out_dirs: list[Path]
    excludes: set[Path]
    merge: set[Path]
    log_level: int = logging.INFO
    merge_readme: bool = False

    def log_debug(self, msg, *_args, **_kwargs):
        if self.log_level <= logging.DEBUG:
            logging.debug(msg, *_args, **_kwargs)

    def log_info(self, msg, *_args, **_kwargs):
        if self.log_level <= logging.INFO:
            logging.info(msg, *_args, **_kwargs)

    def log_warning(self, msg, *_args, **_kwargs):
        if self.log_level <= logging.WARNING:
            logging.warning(msg, *_args, **_kwargs)

    def log_error(self, msg, *_args, **_kwargs):
        if self.log_level <= logging.ERROR:
            logging.error(msg, *_args, **_kwargs)

    def log_critical(self, msg, *_args, **_kwargs):
        if self.log_level <= logging.CRITICAL:
            logging.critical(msg, *_args, **_kwargs)

    def log_exception(self, msg, *_args, exc_info=True, **_kwargs):
        if self.log_level <= logging.ERROR:
            logging.error(msg, *_args, exc_info=exc_info, **_kwargs)


def create_config(raw_cfg: AnyDict) -> Config | None:
    if raw_cfg.get("only_in_release", False) and not args.release:
        return None
    log_level: int | str = raw_cfg.get("log_level", logging.INFO)
    if isinstance(log_level, str):
        log_level = logging.getLevelNamesMapping()[log_level]
    _out_dirs = raw_cfg.get("extra_out_dirs", [])
    if isinstance(_out_dirs, str):
        _out_dir = Path(_out_dirs)
        _out_dirs = [_out_dir] if _out_dir.is_absolute() else []
    elif isinstance(_out_dirs, list):
        _out_dirs = [p for p in map(Path, _out_dirs) if p.is_absolute()]
    else:
        _out_dirs = []

    cfg = Config(
        str(raw_cfg.get("name", "<unnamed>")),
        Path(raw_cfg.get("src_dir", "src/")),
        Path(raw_cfg.get("out_dir", "out/")),
        _out_dirs,
        get_paths(raw_cfg.get("excludes", [])),
        get_paths(raw_cfg.get("merge", [])),
        log_level,
        raw_cfg.get("merge_readme", False),
    )
    cfg.log_info("%s: starting...", cfg.name)
    if raw_cfg.get("clear", True):
        shutil.rmtree(cfg.out_dir, ignore_errors=True)
    os.makedirs(cfg.out_dir, exist_ok=True)
    return cfg


@dataclass
class InputInfo:
    """Information about input. May change after init."""

    path: Path
    blocking_mode: bool
    zip_mode: bool
    excludes: set[Path]
    includes: dict[Path, Path | None]

    def copy(self, **changes):
        return replace(self, **changes)


ENCODER = JSONEncoder(ensure_ascii=False, indent=None, separators=(",", ":"))


@contextmanager
def timer(cfg: Config, operation: str, target: Any):
    start = time.time()
    try:
        yield
    finally:
        cfg.log_debug('%s: %s "%s" costs %ss', cfg.name, operation, target, time.time() - start)


@contextmanager
def error_context(cfg: Config, operation: str, target: Path):
    try:
        yield
    except Exception as e:
        cfg.log_error("Error in %s at %s: %s", operation, target, e, exc_info=True)
        raise


def is_empty(p: Path):
    return p == Path(".") or p == Path()


def join_path_s(path: Path, may_path: Path | None) -> Path:
    return path if may_path is None else path / may_path


def load_json(path: Path, *_args, **_kwargs) -> Any:
    with open(path, *_args, **_kwargs) as f:
        json_data = json.load(f)
        return json_data


def get_paths(
    obj: list[AnyDict | str] | AnyDict | str,
    paths: set[Path] | None = None,
    path: Path = Path(),
):
    if paths is None:
        paths = set[Path]()
    if isinstance(obj, str):
        paths.add(path / obj)
    elif isinstance(obj, list):
        for o in obj:
            get_paths(o, paths, path)
    else:
        _path = join_path_s(path, obj.get("path"))

        if obj.get("type") == "load_json" and op.isfile(_path):
            get_paths(load_json(_path), paths, _path.parent)
        elif "extras" in obj:
            get_paths(obj["extras"], paths, _path)
        else:
            paths.add(_path)

    return paths


def get_paths_with_out(
    obj: list[AnyDict | str] | AnyDict | str,
    paths: dict[Path, Path | None] | None = None,
    i_path: Path = Path(),
    o_path: Path = Path(),
):
    if paths is None:
        paths = {}
    if isinstance(obj, str):
        paths[i_path / obj] = None if is_empty(o_path) else o_path / obj
    elif isinstance(obj, list):
        for o in obj:
            get_paths_with_out(o, paths, i_path)
    else:
        _i_path = join_path_s(i_path, obj.get("path"))
        _o_path = join_path_s(o_path, obj.get("out_path"))
        if obj.get("type") == "load_json" and op.isfile(_i_path):
            get_paths_with_out(load_json(_i_path), paths, _i_path.parent, _o_path)
        elif "extras" in obj:
            get_paths_with_out(obj["extras"], paths, _i_path, _o_path)
        else:
            paths[_i_path] = _o_path

    return paths


def get_inputs(
    obj: list[AnyDict | str] | AnyDict | str,
    cfg: Config,
    inputs: list[InputInfo] | None = None,
    ii: InputInfo | None = None,
) -> list[InputInfo]:
    if inputs is None:
        inputs = list[InputInfo]()
    if ii is None:
        ii = InputInfo(Path(cfg.src_dir), False, True, set[Path](), {})

    if isinstance(obj, list):
        for o in obj:
            get_inputs(o, cfg, inputs, ii.copy())
    elif isinstance(obj, str):
        inputs.append(ii.copy(path=ii.path / obj))
    else:
        _path = join_path_s(ii.path, obj.get("path"))
        new_ii = ii.copy(
            zip_mode=obj.get("zip_mode", ii.zip_mode),
            blocking_mode=obj.get("mode", ii.blocking_mode),
            excludes=ii.excludes.copy() | get_paths(obj.get("excludes", [])),
            includes=ii.includes.copy() | get_paths_with_out(obj.get("includes", [])),
        )
        if obj.get("type") == "load_json" and _path.is_file():
            new_ii.path = _path.parent
            get_inputs(load_json(_path), cfg, inputs, new_ii)
        else:
            new_ii.path = _path
            if "extras" in obj:
                get_inputs(obj["extras"], cfg, inputs, new_ii)
            else:
                inputs.append(new_ii)
    return inputs


def full_match(path: Path, iterable: Iterable[Any]):
    for pattern in iterable:
        if path.full_match(pattern):
            return True
    return False


def not_excluded(path_o: Path, cfg: Config, excludes: set[Path]):
    """Excluding files.
    return False if matched exclude.
    """
    if full_match(path_o, excludes):
        cfg.log_debug('%s: excluded "%s"', cfg.name, path_o)
        return False
    if full_match(path_o, cfg.excludes):
        cfg.log_debug('%s: excluded "%s" by default', cfg.name, path_o)
        return False
    return True


def not_blocked(path_o: Path, cfg: Config, ii: InputInfo):
    if ii.blocking_mode:
        if not full_match(path_o, list(ii.includes.keys())):
            return False
    else:
        if full_match(path_o, list(ii.includes.keys())):
            return True
    return not_excluded(path_o, cfg, ii.excludes)


def moving(o_path: Path, cfg: Config, ii: InputInfo) -> str:
    m_path = ii.includes.get(o_path, None)
    if m_path and not is_empty(m_path):
        cfg.log_debug('Moved "%s" to "%s"', o_path, m_path)
    return str(m_path or o_path)


def encode_bytes(obj: Any) -> bytes:
    return bytes(ENCODER.encode(obj), "utf-8")


def optimize_png(stream: IO[bytes]):
    img = Image.open(stream)
    try:  # necessary
        output = io.BytesIO()
        img.save(output, "png", optimize=True)
        return output.getvalue()
    except:
        return stream.read()


def store(
    storage: BytesDict,
    cfg: Config,
    ii: InputInfo,
    stream: IO[bytes],
    o_path: Path,
):
    moved = moving(o_path, cfg, ii)
    result = bytes()
    if moved.endswith(".json") and moved in storage and full_match(o_path, cfg.merge):
        stored = json.loads(storage[moved])
        target = json.load(stream)
        if isinstance(stored, dict) and isinstance(target, dict):
            result = encode_bytes(stored | target)
            return
    elif release and moved.endswith(".json"):
        result = encode_bytes(json.loads(storage[moved]))
    elif moved.endswith(".json*.pbpatch"):
        if moved.removesuffix(".pbpatch") in storage:
            result = encode_bytes(jsonpatch.apply_patch(json.loads(storage[moved]), stream.read(), True))
        else:
            cfg.log_warning(".pbpatch %s does not find a file to patch", o_path)
    elif cfg.merge_readme and moved.lower().endswith("readme.md") and moved in storage:
        endl = b"" if storage[moved].endswith(b"\n") else b"\n"
        result = storage[moved] + endl + stream.read()
        return
    elif moved.endswith(".png") and args.release:
        result = optimize_png(stream)
        stream.seek(0)
        cfg.log_debug("%s => %s", len(stream.read()), len(result))
    else:
        result = stream.read()
    storage[moved] = result
    return


def input_file(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process file input."""
    if not ii.zip_mode or not ii.path.name.endswith(".zip"):
        cfg.log_debug("Loading single file %s", ii.path)
        with open(ii.path, "rb") as f:
            store(storage, cfg, ii, f, Path(ii.path.name))
        return

    with zipfile.ZipFile(file=ii.path, mode="r") as zipf:
        cfg.log_debug("Loading zip file %s", ii.path)
        paths = [
            _i.filename for _i in zipf.filelist if not _i.is_dir() and not_blocked(Path(_i.filename), cfg, ii)
        ]

        def on_filename(path_io: str):
            with zipf.open(str(path_io)) as f:
                store(storage, cfg, ii, f, Path(path_io))

        with ThreadPoolExecutor() as tpe:
            for path in paths:
                tpe.submit(on_filename, path)


def input_dir(storage: BytesDict, cfg: Config, ii: InputInfo):
    base_path = Path(ii.path)
    all_files = [
        (p, p.relative_to(base_path))
        for p in base_path.rglob("*")
        if p.is_file() and not_blocked(p.relative_to(base_path), cfg, ii)
    ]

    def on_file(path: Path, o_path: Path):
        with path.open("rb") as f:
            store(storage, cfg, ii, f, o_path)

    with ThreadPoolExecutor() as tpe:
        for i_path, o_path in all_files:
            tpe.submit(on_file, i_path, o_path)


def cfg_tree(cfg: Config, tree: AnyDict, storage: BytesDict):
    name = tree.get("name", "<unknown>")
    removes = get_paths(tree.get("removes", []))
    for k in list(storage.keys()):
        if full_match(Path(k), removes):
            cfg.log_debug("Removed %s from storage", k)
            storage.pop(k)

    inputs: str | AnyDict | list[str | AnyDict] = tree["inputs"]
    extra_out = tree.get("extra_out", True)

    with timer(cfg, "Loading", name):
        # no multithread here because new inputs may override or attach to old file
        for ii in get_inputs(inputs, cfg):
            isdir = os.path.isdir(ii.path)
            isfile = os.path.isfile(ii.path)
            if not isdir and not isfile:
                cfg.log_error("%s is not dir or file", ii.path)
                continue
            if isdir:
                with error_context(cfg, "input dir", ii.path):
                    input_dir(storage, cfg, ii)
            if isfile:
                with error_context(cfg, "input file", ii.path):
                    input_file(storage, cfg, ii)

    def on_output():
        o_path = cfg.out_dir / (tree["output"] + ".zip")
        os.makedirs(o_path.parent, exist_ok=True)

        with timer(cfg, "Zipping", name):
            # no multithread here because ZipFile does not support that
            with ZipFile(o_path, "w", 8, True, 9 if args.release else 1) as zipf:
                for k, v in storage.items():
                    zipf.writestr(k, v)
        size = o_path.stat().st_size >> 10
        cfg.log_info('%s: "%s" completed (%s files, %s KiB)', cfg.name, o_path.name, len(storage), size)
        if not extra_out:
            return
        for extra_out_dir in cfg.extra_out_dirs:
            shutil.copy(o_path, extra_out_dir)
        if cfg.extra_out_dirs != 0:
            cfg.log_debug('Copied "%s" to "%s"', o_path, [str(p) for p in cfg.extra_out_dirs])

    def on_children():
        children: AnyDict | list[AnyDict] = tree["children"]
        if isinstance(children, list):
            with ThreadPoolExecutor() as tpe:
                for i in children:
                    tpe.submit(cfg_tree, cfg, i, storage.copy())
        else:
            cfg_tree(cfg, children, storage.copy())

    if "children" in tree and "output" in tree:
        th = Thread(target=on_children)
        th.start()
        on_output()
        th.join()
    elif "children" in tree:
        on_children()
    elif "output" in tree:
        on_output()


def cfg_root(raw_cfg: list[AnyDict] | AnyDict):
    """Process config root."""
    if isinstance(raw_cfg, list):
        with ThreadPoolExecutor() as tpe:
            for item in raw_cfg:
                tpe.submit(cfg_root, item)
        return

    if not (cfg := create_config(raw_cfg)):
        return

    tree: AnyDict | list[AnyDict] = raw_cfg["tree"]

    if isinstance(tree, list):
        with ThreadPoolExecutor() as tpe:
            for j in tree:
                tpe.submit(cfg_tree, cfg, j, {})
    else:
        cfg_tree(cfg, tree, {})


def setup_log():
    if op.isfile(args.log):
        os.makedirs("logs", exist_ok=True)
        _t = dt.fromtimestamp(os.stat(args.log).st_mtime).strftime("%Y-%m-%d_%H-%M-%S")
        shutil.copy2(args.log, f"logs/{_t} {op.basename(args.log)}")
    logger.setLevel(logging.DEBUG)
    _stdout = logging.StreamHandler(sys.stdout)
    _stdout.setLevel(logging.INFO)

    _stdout.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S"))
    logger.addHandler(_stdout)

    _file = logging.FileHandler(args.log, mode="w")
    _file.setLevel(logging.DEBUG)
    _file.setFormatter(logging.Formatter("[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s", "%H:%M:%S"))
    logger.addHandler(_file)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--release", action="store_true")
    parser.add_argument("-d", "--dir", default=os.path.dirname(__file__))
    parser.add_argument("-c", "--cfg", default="config.json")
    parser.add_argument("-l", "--log", default="build.log")
    return parser.parse_args()


args = parse_args()
os.chdir(args.dir)
setup_log()
tp_start = dt.now()
cfg_root(load_json(args.cfg, "rb"))
logging.info("Build stops at %s, total cost %s.", dt.now(), dt.now() - tp_start)
