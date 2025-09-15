from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Thread
import shutil
import json
import logging
import sys
import time
import os


from os import path as op
from datetime import datetime as dt
from dataclasses import dataclass, replace
from typing import IO, Any
from json.encoder import JSONEncoder

# import fastzipfile
# from fastzipfile import zipfile
import zipfile

AnyDict = dict[str, Any]
BytesDict = dict[str, bytes]

logger = logging.getLogger()
release: bool = False
packsquash_path: str | None = None

ENCODER = JSONEncoder(ensure_ascii=False, indent=None, separators=(",", ":"))


@dataclass(frozen=True)
class Config:
    """A config entry"""

    name: str
    src_dir: str
    out_dir: str
    extra_out_dirs: list[str] | str
    exclude_ext: tuple[str, ...]
    default_excludes: set[str]
    default_merge: set[str]
    log_level: int = logging.INFO
    compression: int = 0
    compresslevel: int | None = None

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
    excludes: set[str]
    includes: dict[str, str | None]
    # reformat: JSONEncoder | None = None

    def copy(self, **changes):
        return replace(self, **changes)


class Timer:
    """Timer for debug logging."""

    def __init__(self, cfg: Config, arg1: str, arg2: Any):
        self.cfg = cfg
        self.arg1 = arg1
        self.arg2 = arg2
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None):
        if self.start_time is not None:
            self.cfg.log_debug(
                '%s: %s "%s" costs %ss',
                self.cfg.name,
                self.arg1,
                self.arg2,
                time.time() - self.start_time,
            )


def norm_path(path: str) -> str:
    return Path(path).as_posix()


def join_path(path: str, /, *paths: str) -> str:
    return Path(path).joinpath(*paths).as_posix()


def get_paths_with_output(
    obj: list[AnyDict | str] | AnyDict | str,
    includes: dict[str, str | None] | None = None,
    path: str = "",
    out_path: str = "",
):
    """Process includes."""
    if includes is None:
        includes = {}
    if isinstance(obj, str):
        includes[join_path(path, obj)] = (
            join_path(out_path, obj) if len(out_path) != 0 else None
        )
    elif isinstance(obj, list):
        for o in obj:
            get_paths_with_output(o, includes, path)
    else:
        new_path = op.join(path, obj["path"]) if "path" in obj else path
        new_out_path = (
            op.join(out_path, obj["out_path"]) if "out_path" in obj else out_path
        )
        if "extras" in obj:
            get_paths_with_output(obj["extras"], includes, new_path, new_out_path)
        else:
            includes[norm_path(new_path)] = norm_path(new_out_path)

    return includes


def get_paths(
    obj: list[AnyDict | str] | AnyDict | str,
    paths: set[str] | None = None,
    path: str = "",
):
    """Process excludes."""
    if paths is None:
        paths = set[str]()
    if isinstance(obj, str):
        paths.add(join_path(path, obj))
    elif isinstance(obj, list):
        for o in obj:
            get_paths(o, paths, path)
    else:
        new_path = op.join(path, obj["path"]) if "path" in obj else path
        if "extras" in obj:
            get_paths(obj["extras"], paths, new_path)
        else:
            paths.add(norm_path(new_path))

    return paths


def get_inputs(
    obj: list[AnyDict | str] | AnyDict | str,
    inputs: list[InputInfo] | None,
    ii: InputInfo | None,
    cfg: Config,
) -> list[InputInfo]:
    """Process excludes."""
    if inputs is None:
        inputs = list[InputInfo]()
    if ii is None:
        ii = InputInfo(cfg.src_dir, False, True, set[str](), {})

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
        # reformat: AnyDict | JSONEncoder | None = obj.get("reformat", None)
        # if isinstance(reformat, dict):
        #    reformat = JSONEncoder(
        #        skipkeys=reformat.get("skipkeys", False),
        #        ensure_ascii=reformat.get("ensure_ascii", False),
        #        check_circular=reformat.get("check_circular", True),
        #        allow_nan=reformat.get("allow_nan", True),
        #        indent=reformat.get("indent", None),
        #        sort_keys=reformat.get("sort_keys", True),
        #        separators=reformat.get("separators", (",", ":")),
        #        default=reformat.get("default", None),
        #    )
        new_ii = ii.copy(
            path=new_path,
            zip_mode=obj.get("zip_mode", ii.zip_mode),
            blocking_mode=obj.get("mode", ii.blocking_mode),
            excludes=new_excludes,
            includes=new_includes,
            # reformat=reformat,
        )
        if "extras" in obj:
            get_inputs(obj["extras"], inputs, new_ii, cfg)
        else:
            inputs.append(new_ii)

    return inputs


def not_excluded(opath: str, cfg: Config, excludes: set[str]):
    """Excluding files.
    return False if matched exclude.
    """
    if opath.endswith(cfg.exclude_ext):
        cfg.log_debug('%s: Excluded "%s" by extension', cfg.name, opath)
        return False
    if opath.startswith(tuple(excludes)):
        cfg.log_debug('%s: Excluded "%s" by relative path', cfg.name, opath)
        excludes.remove(opath)
        return False
    if opath.startswith(tuple(cfg.default_excludes)):
        cfg.log_debug('%s: Excluded "%s" by default', cfg.name, opath)
        return False
    return True


def not_blocked(opath: str, cfg: Config, ii: InputInfo):
    if ii.blocking_mode:
        if not any(opath.startswith(include) for include in ii.includes.keys()):
            return False
    else:
        if any(opath.startswith(include) for include in ii.includes.keys()):
            return True
    return not_excluded(opath, cfg, ii.excludes)


def moving(opath: str, cfg: Config, ii: InputInfo) -> str:
    mpath = ii.includes.get(opath, None)
    if mpath is not None:
        cfg.log_debug('Moved "%s" to "%s"', opath, mpath)
    return mpath or opath


def check_excludes(cfg: Config, ii: InputInfo):
    if len(ii.excludes) != 0:
        cfg.log_warning(
            "%s files in %s not excluded: %s",
            len(ii.excludes),
            ii.path,
            ii.excludes,
        )


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
        if opath.startswith(tuple(cfg.default_merge)) and moved in storage:
            original = json.loads(storage[moved])
            target = json.load(stream)
            if isinstance(original, dict) and isinstance(target, dict):
                original.update(target)
                storage[moved] = bytes(ENCODER.encode(original), "utf-8")
                return
        if release:
            storage[moved] = bytes(ENCODER.encode(json.load(stream)), "utf-8")
            return
    storage[moved] = stream.read()
    return


def input_file(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process file input."""
    try:
        if not ii.zip_mode or not ii.path.endswith(".zip"):
            cfg.log_debug(f"Loading single file {ii.path}")
            with open(ii.path, "rb") as f:
                store_file(storage, cfg, ii, f, ii.path, ii.path)
            check_excludes(cfg, ii)
            return
        with zipfile.ZipFile(file=ii.path, mode="r") as zipf:
            cfg.log_debug(f"Loading zip file {ii.path}")

            def on_zipinfo(zinfo: zipfile.ZipInfo):
                iopath = zinfo.filename
                if not_blocked(iopath, cfg, ii):
                    with zipf.open(iopath) as f:
                        store_file(storage, cfg, ii, f, iopath, iopath)

            with ThreadPoolExecutor() as tpe:
                for zinfo in zipf.filelist:
                    if zinfo.is_dir():
                        continue
                    tpe.submit(on_zipinfo, zinfo)
            check_excludes(cfg, ii)
    except Exception as e:
        cfg.log_error("Error processing file %s: %s", ii.path, e, exc_info=True)


def input_dir(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process directory input."""
    cfg.log_debug(f"Loading directory {ii.path}")
    try:
        for root, _, files in os.walk(ii.path):

            def on_file(file: str):
                ipath = op.normpath(op.join(root, file))
                opath = op.relpath(ipath, ii.path).replace(os.sep, "/")
                if not_blocked(opath, cfg, ii):
                    with open(ipath, "rb") as f:
                        store_file(storage, cfg, ii, f, ipath, opath)

            with ThreadPoolExecutor() as tpe:
                for file in files:
                    tpe.submit(on_file, file)
        check_excludes(cfg, ii)
    except Exception as e:
        cfg.log_error("Error processing directory %s: %s", ii.path, e, exc_info=True)


def cfg_tree(
    cfg: Config,
    tree: AnyDict,
    storage: BytesDict,
):
    """Process config tree."""
    try:
        inputs: str | AnyDict | list[str | AnyDict] = tree["inputs"]

        for ii in get_inputs(inputs, None, None, cfg):
            if os.path.isdir(ii.path):
                input_dir(storage, cfg, ii)
            elif os.path.isfile(ii.path):
                input_file(storage, cfg, ii)
            else:
                cfg.log_error(f"{ii.path} is not dir or file")

        def on_output():

            filepath = Path(tree["output"] + ".zip")
            out_path = Path(cfg.out_dir, filepath)

            os.makedirs(op.dirname(out_path), exist_ok=True)
            with Timer(cfg, "Zipping", filepath):
                with zipfile.ZipFile(
                    out_path,
                    "w",
                    compression=cfg.compression,
                    compresslevel=cfg.compresslevel,
                ) as zipm:
                    for k, v in storage.items():
                        zipm.writestr(k, v)
            cfg.log_info(
                '%s: "%s" completed (%s files, %s KiB)',
                cfg.name,
                filepath,
                len(storage),
                out_path.stat().st_size >> 10,
            )

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
    except Exception as e:
        cfg.log_error("Error in cfg_tree for config %s: %s", cfg.name, e, exc_info=True)


def cfg_root(raw_cfg: list[AnyDict] | AnyDict):
    """Process config root."""
    if isinstance(raw_cfg, list):
        with ThreadPoolExecutor() as tpe:
            for item in raw_cfg:
                tpe.submit(cfg_root, item)
        return
    if raw_cfg.get("only_in_release", False) and not release:
        return
    log_level: int | str = raw_cfg.get("log_level", logging.INFO)
    if isinstance(log_level, str):
        log_level = logging.getLevelNamesMapping()[log_level]

    cfg = Config(
        raw_cfg.get("name", "<unnamed>"),
        raw_cfg.get("src_dir", "src/"),
        raw_cfg.get("out_dir", "out/"),
        raw_cfg.get("extra_out_dirs", []),
        raw_cfg.get("exclude_ext", (".py", ".backup", ".temp")),
        get_paths(raw_cfg.get("default_excludes", [])),
        get_paths(raw_cfg.get("default_merge", [])),
        log_level,
        raw_cfg.get("compression", 0),
        raw_cfg.get("compresslevel", None),
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


def try_get_arg(s: str, d: str) -> str:
    try:
        args = sys.argv[1:]
        return args[args.index(s) + 1]
    except:
        return d


if __name__ == "__main__":
    try:
        release = "--release" in sys.argv[1:]
        dir_path = try_get_arg("--dir", op.dirname(__file__))
        cfg_path = try_get_arg("--cfg", "config.json")
        log_path = try_get_arg("--log", "build.log")
        packsquash_path = try_get_arg("--packsquash", "packsquash.exe")

        os.chdir(dir_path)

        if op.isfile(log_path):
            os.makedirs("logs", exist_ok=True)

            with open(log_path, "rb") as log:
                with open(
                    f"logs/{dt.fromtimestamp(os.stat(log_path).st_mtime).strftime("%Y-%m-%d_%H-%M-%S")} {op.basename(log_path)}",
                    "xb",
                ) as log_archive:
                    log_archive.write(log.read())

        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%H:%M:%S"
            )
        )

        file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
                datefmt="%H:%M:%S",
            )
        )

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        tp_start = dt.now()

        with open(cfg_path, "r", encoding="utf-8") as cfg_file:
            config_data = json.load(cfg_file)

        cfg_root(config_data)

        logging.info("Build stops at %s, total cost %s.", dt.now(), dt.now() - tp_start)

    except Exception as e:
        logging.error("Error: %s", e, exc_info=True)
