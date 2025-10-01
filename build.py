from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Thread
import shutil
import json
import logging
import sys
import time
import os
import argparse
import zipfile


from os import path as op
from datetime import datetime as dt
from dataclasses import dataclass, replace
from typing import IO, Any
from json.encoder import JSONEncoder
from contextlib import contextmanager


AnyDict = dict[str, Any]
BytesDict = dict[str, bytes]

logger = logging.getLogger()
release: bool = False

ENCODER = JSONEncoder(ensure_ascii=False, indent=None, separators=(",", ":"))


@dataclass(frozen=True)
class Config:
    """A config entry"""

    name: str
    src_dir: str
    out_dir: str
    extra_out_dirs: list[str] | str
    excludes: tuple
    merge: tuple
    log_level: int = logging.INFO

    def log_debug(self, msg, *args, **kwargs):
        if self.log_level <= logging.DEBUG:
            logging.debug(msg, *args, **kwargs)

    def log_info(self, msg, *args, **kwargs):
        if self.log_level <= logging.INFO:
            logging.info(msg, *args, **kwargs)

    def log_warning(self, msg, *args, **kwargs):
        if self.log_level <= logging.WARNING:
            logging.warning(msg, *args, **kwargs)

    def log_error(self, msg, *args, **kwargs):
        if self.log_level <= logging.ERROR:
            logging.error(msg, *args, **kwargs)

    def log_critical(self, msg, *args, **kwargs):
        if self.log_level <= logging.CRITICAL:
            logging.critical(msg, *args, **kwargs)

    def log_exception(self, msg, *args, exc_info=True, **kwargs):
        if self.log_level <= logging.ERROR:
            logging.error(msg, *args, exc_info=exc_info, **kwargs)


@dataclass
class InputInfo:
    """Information about input. May change after init."""

    path: str
    blocking_mode: bool
    zip_mode: bool
    excludes: tuple
    includes: dict[str, str | None]
    # reformat: JSONEncoder | None = None

    def copy(self, **changes):
        return replace(self, **changes)


@contextmanager
def timer(cfg: Config, operation: str, target: Any):
    start_time = time.time()
    try:
        yield
    finally:
        cfg.log_debug(
            '%s: %s "%s" costs %ss',
            cfg.name,
            operation,
            target,
            time.time() - start_time,
        )


def norm_path(path: str) -> str:
    return Path(path).as_posix()


def join_path(path: str, /, *paths: str) -> str:
    return Path(path).joinpath(*paths).as_posix()


def join_path_from_file(path: str, s: str) -> str:
    return join_path(path, op.relpath(op.dirname(s), path))


def get_from_file(obj: AnyDict, path: str):
    _type = obj.get("type", None)
    if _type == "load_json" and op.isfile(path):
        with open(path, "r") as f:
            json_data = json.load(f)
            return json_data
    return None


def get_paths(
    obj: list[AnyDict | str] | AnyDict | str,
    paths: set[str] | None = None,
    path: str = "",
):
    if paths is None:
        paths = set[str]()
    if isinstance(obj, str):
        paths.add(join_path(path, obj))
    elif isinstance(obj, list):
        for o in obj:
            get_paths(o, paths, path)
    else:
        new_path = op.join(path, obj["path"]) if "path" in obj else path
        _load_json = get_from_file(obj, new_path)
        if _load_json is not None:
            get_paths(_load_json, paths, join_path_from_file(path, new_path))
        elif "extras" in obj:
            get_paths(obj["extras"], paths, new_path)
        else:
            paths.add(norm_path(new_path))

    return paths


def get_paths_with_output(
    obj: list[AnyDict | str] | AnyDict | str,
    paths_w_o: dict[str, str | None] | None = None,
    path: str = "",
    out_path: str = "",
):
    if paths_w_o is None:
        paths_w_o = {}
    if isinstance(obj, str):
        paths_w_o[join_path(path, obj)] = (
            join_path(out_path, obj) if len(out_path) != 0 else None
        )
    elif isinstance(obj, list):
        for o in obj:
            get_paths_with_output(o, paths_w_o, path)
    else:
        new_path = op.join(path, obj["path"]) if "path" in obj else path
        new_out_path = (
            op.join(out_path, obj["out_path"]) if "out_path" in obj else out_path
        )
        _load_json = get_from_file(obj, new_path)
        if _load_json is not None:
            get_paths_with_output(
                _load_json, paths_w_o, join_path_from_file(path, new_path), new_out_path
            )
        elif "extras" in obj:
            get_paths_with_output(obj["extras"], paths_w_o, new_path, new_out_path)
        else:
            paths_w_o[norm_path(new_path)] = norm_path(new_out_path)

    return paths_w_o


def get_inputs(
    obj: list[AnyDict | str] | AnyDict | str,
    inputs: list[InputInfo] | None,
    ii: InputInfo | None,
    cfg: Config,
) -> list[InputInfo]:
    if inputs is None:
        inputs = list[InputInfo]()
    if ii is None:
        ii = InputInfo(cfg.src_dir, False, True, (), {})

    if isinstance(obj, list):
        for o in obj:
            get_inputs(o, inputs, ii.copy(), cfg)
    elif isinstance(obj, str):
        new_path = join_path(ii.path, obj)
        inputs.append(ii.copy(path=new_path))
    else:
        new_path = op.join(ii.path, obj["path"]) if "path" in obj else ii.path
        new_excludes = get_paths(obj.get("excludes", []))
        new_excludes.update(ii.excludes)
        new_includes = get_paths_with_output(obj.get("includes", []))
        new_includes.update(ii.includes)

        new_ii = ii.copy(
            zip_mode=obj.get("zip_mode", ii.zip_mode),
            blocking_mode=obj.get("mode", ii.blocking_mode),
            excludes=tuple(new_excludes),
            includes=new_includes,
        )

        _load_json = get_from_file(obj, new_path)
        if _load_json is not None:
            new_ii.path = join_path_from_file(ii.path, new_path)
            get_inputs(
                _load_json,
                inputs,
                new_ii,
                cfg,
            )

        new_ii.path = new_path
        if "extras" in obj:
            get_inputs(obj["extras"], inputs, new_ii, cfg)
        else:
            inputs.append(new_ii)

    return inputs


def full_match(path: Path, container: Any):
    for pattern in container:
        if path.full_match(pattern):
            return True
    return False


def not_excluded(opath: Path, cfg: Config, excludes: tuple):
    """Excluding files.
    return False if matched exclude.
    """
    # if opath.endswith(cfg.exclude_ext):
    #    cfg.log_debug('%s: exclude "%s" by extension', cfg.name, opath)
    #    return False
    if full_match(opath, excludes):
        cfg.log_debug('%s: excluded "%s"', cfg.name, opath)
        return False
    if full_match(opath, cfg.excludes):
        cfg.log_debug('%s: exclude "%s" by default', cfg.name, opath)
        return False
    return True


def not_blocked(opath: Path, cfg: Config, ii: InputInfo):
    if ii.blocking_mode:
        if not full_match(opath, list(ii.includes.keys())):
            return False
    else:
        if full_match(opath, list(ii.includes.keys())):
            return True
    return not_excluded(opath, cfg, ii.excludes)


def moving(opath: str, cfg: Config, ii: InputInfo) -> str:
    mpath = ii.includes.get(opath, None)
    if mpath is not None:
        cfg.log_debug('Moved "%s" to "%s"', opath, mpath)
    return mpath or opath


def store_file(
    storage: BytesDict,
    cfg: Config,
    ii: InputInfo,
    stream: IO[bytes],
    ipath: str,
    opath: str,
):
    moved = moving(opath, cfg, ii)
    if ipath.endswith(".json"):
        if moved in storage and full_match(Path(opath), cfg.merge):
            original = json.loads(storage[moved])
            target = json.load(stream)
            if isinstance(original, dict) and isinstance(target, dict):
                original.update(target)
                storage[moved] = bytes(ENCODER.encode(original), "utf-8")
                return
        if args.release:
            storage[moved] = bytes(ENCODER.encode(json.load(stream)), "utf-8")
            return
    storage[moved] = stream.read()
    return


def input_file(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process file input."""
    if not ii.zip_mode or not ii.path.endswith(".zip"):
        cfg.log_debug("Loading single file %s", ii.path)
        with open(ii.path, "rb") as f:
            store_file(storage, cfg, ii, f, ii.path, op.basename(ii.path))
        return
    with zipfile.ZipFile(file=ii.path, mode="r") as zipf:
        cfg.log_debug("Loading zip file %s", ii.path)

        def on_zipinfo(zinfo: zipfile.ZipInfo):
            iopath = zinfo.filename
            if not_blocked(Path(iopath), cfg, ii):
                with zipf.open(iopath) as f:
                    store_file(storage, cfg, ii, f, iopath, iopath)

        with ThreadPoolExecutor() as tpe:
            for zinfo in zipf.filelist:
                if zinfo.is_dir():
                    continue
                tpe.submit(on_zipinfo, zinfo)


def input_dir(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process directory input."""
    cfg.log_debug(f"Loading directory {ii.path}")
    base_path = Path(ii.path)
    all_files = [p for p in base_path.rglob("*") if p.is_file()]

    def on_file(file_path: Path):
        opath = file_path.relative_to(base_path)
        if not_blocked(opath, cfg, ii):
            with open(file_path, "rb") as f:
                store_file(storage, cfg, ii, f, file_path.as_posix(), opath.as_posix())

    with ThreadPoolExecutor() as tpe:
        for file_path in all_files:
            tpe.submit(on_file, file_path)


def cfg_tree(cfg: Config, tree: AnyDict, storage: BytesDict):
    removes = get_paths(tree.get("removes", []))
    for k in list(storage.keys()):
        if full_match(Path(k), removes):
            cfg.log_debug("Removed %s from storage", k)
            storage.pop(k)

    inputs: str | AnyDict | list[str | AnyDict] = tree["inputs"]
    extra_out = tree.get("extra_out", True)

    for ii in get_inputs(inputs, None, None, cfg):
        isdir = os.path.isdir(ii.path)
        isfile = os.path.isfile(ii.path)
        if not isdir and not isfile:
            cfg.log_error("%s is not dir or file", ii.path)
        if isdir:
            try:
                input_dir(storage, cfg, ii)
            except Exception as e:
                cfg.log_error("Error at %s: %s", ii.path, e, exc_info=True)
        if isfile:
            try:
                input_file(storage, cfg, ii)
            except Exception as e:
                cfg.log_error("Error at %s: %s", ii.path, e, exc_info=True)

    def on_output():
        filepath = Path(tree["output"] + ".zip")
        out_path = Path(cfg.out_dir, filepath)
        os.makedirs(op.dirname(out_path), exist_ok=True)
        with timer(cfg, "Zipping", filepath):

            with zipfile.ZipFile(
                out_path,
                "w",
                zipfile.ZIP_DEFLATED,
                compresslevel=9 if args.release else 1,
            ) as vzip:
                for k, v in storage.items():
                    vzip.writestr(k, v)
        cfg.log_info(
            '%s: "%s" completed (%s files, %s KiB)',
            cfg.name,
            filepath,
            len(storage),
            out_path.stat().st_size >> 10,
        )
        if not extra_out:
            return
        if isinstance(cfg.extra_out_dirs, list):
            for extra_out_dir in cfg.extra_out_dirs:
                shutil.copy(out_path, extra_out_dir)
        else:
            shutil.copy(out_path, cfg.extra_out_dirs)
        if len(cfg.extra_out_dirs) != 0:
            cfg.log_debug('Copied "%s" to "%s"', out_path, cfg.extra_out_dirs)

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
    if raw_cfg.get("only_in_release", False) and not args.release:
        return
    log_level: int | str = raw_cfg.get("log_level", logging.INFO)
    if isinstance(log_level, str):
        log_level = logging.getLevelNamesMapping()[log_level]

    cfg = Config(
        raw_cfg.get("name", "<unnamed>"),
        raw_cfg.get("src_dir", "src/"),
        raw_cfg.get("out_dir", "out/"),
        raw_cfg.get("extra_out_dirs", []),
        tuple(get_paths(raw_cfg.get("excludes", []))),
        tuple(get_paths(raw_cfg.get("merge", []))),
        log_level,
    )
    cfg.log_info('== Config "%s" starts ==', cfg.name)
    if raw_cfg.get("clear", True):
        shutil.rmtree(cfg.out_dir, ignore_errors=True)

    os.makedirs(cfg.out_dir, exist_ok=True)
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
        shutil.copy2(
            args.log,
            f"logs/{_t} {op.basename(args.log)}",
        )

    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%H:%M:%S"
        )
    )

    file_handler = logging.FileHandler(args.log, mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
        )
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--dir", default=os.path.dirname(__file__))
    parser.add_argument("--cfg", default="config.json")
    parser.add_argument("--log", default="build.log")
    return parser.parse_args()


args = parse_args()

os.chdir(args.dir)

setup_log()

tp_start = dt.now()

with open(args.cfg, "rb") as _cfg_f:
    config_data = json.load(_cfg_f)

cfg_root(config_data)

logging.info("Build stops at %s, total cost %s.", dt.now(), dt.now() - tp_start)
