from threading import Thread
import zipfile
import shutil
import json
import logging
import sys
import time
import os


from os import path as op
from datetime import datetime as dt
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any, Literal

type AnyDict = dict[str, Any]
type BytesDict = dict[str, bytes]

executor = ThreadPoolExecutor()
logger = logging.getLogger()


@dataclass(frozen=True)
class Config:
    """A config entry"""

    name: str
    src_dir: str
    out_dir: str
    extra_out_dirs: list[str] | str
    exclude_ext: tuple[str, ...]
    default_excludes: set[str]
    debug: bool
    compress: int


type PathType = Literal["dir", "file"] | None


@dataclass
class InputInfo:
    """Information about input. May change after init."""

    path: str
    path_type: PathType
    mode: Literal["include", "exclude"]
    zip_mode: bool
    excludes: set[str]
    includes: dict[str, str | None]

    def copy(
        self,
        path: str | None = None,
        path_type: PathType | None = None,
        mode: Literal["include", "exclude"] | None = None,
        zip_mode: bool | None = None,
        excludes: set[str] | None = None,
        includes: dict[str, str | None] | None = None,
    ):
        return InputInfo(
            path=path or self.path,
            path_type=path_type or self.path_type,
            mode=mode or self.mode,
            zip_mode=zip_mode or self.zip_mode,
            excludes=(excludes or self.excludes).copy(),
            includes=(includes or self.includes).copy(),
        )


def get_path_type(path: str) -> PathType:
    return "dir" if op.isdir(path) else "file" if op.isfile(path) else None


class Timer:
    """Timer for debug logging."""

    def __init__(self, debug: bool, arg0: str, arg1: str, arg2: str):
        self.debug = debug
        self.arg0 = arg0
        self.arg1 = arg1
        self.arg2 = arg2
        self.start_time = None

    def __enter__(self):
        if self.debug:
            self.start_time = time.time()
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None):
        if self.debug and self.start_time is not None:
            logging.debug(
                "%s %s / %s costs %ss",
                self.arg0,
                self.arg1,
                self.arg2,
                time.time() - self.start_time,
            )


def norm_path(path: str) -> str:
    """Normalized path."""
    return op.normpath(path).replace(os.sep, "/")


def join_path(path: str, /, *paths: str) -> str:
    """Normalized join path."""
    return norm_path(op.join(path, *paths))


def process_includes(
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
            process_includes(o, includes, path)
    else:
        new_out_path = (
            op.join(out_path, obj["out_path"]) if "out_path" in obj else out_path
        )
        new_path = op.join(path, obj["path"]) if "path" in obj else path
        if "extras" in obj:
            process_includes(obj["extras"], includes, new_path, new_out_path)
        else:
            includes[norm_path(new_path)] = norm_path(new_out_path)

    return includes


def process_excludes(
    obj: list[AnyDict | str] | AnyDict | str,
    excludes: set[str] | None = None,
    path: str = "",
):
    """Process excludes."""
    if excludes is None:
        excludes = set[str]()
    if isinstance(obj, str):
        excludes.add(join_path(path, obj))
    elif isinstance(obj, list):
        for o in obj:
            process_excludes(o, excludes, path)
    else:
        new_path = op.join(path, obj["path"]) if "path" in obj else path
        if "extras" in obj:
            process_excludes(obj["extras"], excludes, new_path)
        else:
            excludes.add(norm_path(new_path))

    return excludes


def process_inputs(
    obj: list[AnyDict | str] | AnyDict | str,
    inputs: list[InputInfo] | None = None,
    ii: InputInfo | None = None,
):
    """Process excludes."""
    if inputs is None:
        inputs = list[InputInfo]()
    if ii is None:
        ii = InputInfo("", None, "exclude", True, set[str](), {})

    if isinstance(obj, list):
        for o in obj:
            process_inputs(o, inputs, ii.copy())
    elif isinstance(obj, str):
        new_path = join_path(ii.path, obj)
        inputs.append(ii.copy(path=new_path, path_type=get_path_type(new_path)))
    else:
        new_path = op.join(ii.path, obj["path"]) if "path" in obj else ii.path
        new_excludes = process_excludes(obj.get("excludes", []))
        new_excludes.update(ii.excludes)
        new_includes = process_includes(obj.get("includes", []))
        new_includes.update(ii.includes)
        new_ii = ii.copy(
            path=new_path,
            path_type=get_path_type(new_path),
            zip_mode=obj.get("zip_mode", ii.zip_mode),
            mode=obj.get("mode", ii.mode),
            excludes=new_excludes,
            includes=new_includes,
        )
        if "extras" in obj:
            process_inputs(obj["extras"], inputs, new_ii)
        else:
            inputs.append(new_ii)

    return inputs


def excluding(opath: str, cfg: Config, excludes: set[str]):
    """Excluding files.
    return True if matched exclude.
    """
    if opath.endswith(cfg.exclude_ext):
        if cfg.debug:
            logging.debug('Excluded "%s" by extension', opath)
        return True
    if opath.startswith(tuple(excludes)):
        if cfg.debug:
            logging.debug('Excluded "%s" by relative path', opath)
        excludes.remove(opath)
        return True
    if opath.startswith(tuple(cfg.default_excludes)):
        if cfg.debug:
            logging.debug('Excluded "%s" by default', opath)
        return True
    return False


def include_or_exclude(opath: str, cfg: Config, ii: InputInfo):
    return (ii.mode == "exclude" and not excluding(opath, cfg, ii.excludes)) or (
        ii.mode == "include"
        and any(opath.startswith(include) for include in ii.includes.keys())
    )


def move_including(opath: str, cfg: Config, ii: InputInfo) -> str:
    mpath = ii.includes.get(opath, None)
    if mpath is not None and cfg.debug:
        logging.debug('Moved "%s" to "%s"', opath, mpath)
    return mpath or opath


def input_file(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process file input."""
    if not ii.zip_mode or not ii.path.endswith(".zip"):
        with open(ii.path, "rb") as f:
            storage[op.basename(ii.path)] = f.read()
        return
    with zipfile.ZipFile(file=ii.path, mode="r") as zipf:
        for zinfo in zipf.filelist:
            if zinfo.is_dir():
                continue
            iopath = zinfo.filename
            if include_or_exclude(iopath, cfg, ii):
                storage[move_including(iopath, cfg, ii)] = zipf.read(iopath)


def input_dir(storage: BytesDict, cfg: Config, ii: InputInfo):
    """Process directory input."""

    for root, _, files in os.walk(ii.path):
        for file in files:
            ipath = op.normpath(op.join(root, file))
            opath = op.relpath(ipath, ii.path).replace(os.sep, "/")
            if include_or_exclude(opath, cfg, ii):
                with open(ipath, "rb") as f:
                    storage[move_including(opath, cfg, ii)] = f.read()


def cfg_tree(
    cfg: Config,
    tree: AnyDict,
    storage: BytesDict,
    threads: list[ThreadPoolExecutor | Thread],
):
    """Process config tree."""
    inputs: str | AnyDict | list[str | AnyDict] = tree["inputs"]

    for ii in process_inputs(
        inputs, None, InputInfo(cfg.src_dir, None, "exclude", True, set[str](), {})
    ):
        match ii.path_type:
            case "dir":
                input_dir(storage, cfg, ii)
            case "file":
                input_file(storage, cfg, ii)
            case None:
                logging.error("Path %s not found!", ii.path)

        if len(ii.excludes) != 0:
            logging.warning(
                "%s files in %s not excluded: %s",
                len(ii.excludes),
                ii.path,
                ii.excludes,
            )

    def on_output():
        filename = tree["output"] + ".zip"
        out_path = join_path(cfg.out_dir, filename)
        with Timer(cfg.debug, "Zipping", cfg.name, filename):
            with zipfile.ZipFile(
                out_path, "w", zipfile.ZIP_DEFLATED, compresslevel=cfg.compress
            ) as zipf:
                for k, v in storage.items():
                    zipf.writestr(k, v)
        logging.info(
            '%s: "%s" completed (%s files, %s KiB)',
            cfg.name,
            filename,
            len(storage),
            op.getsize(out_path) >> 10,
        )

        if isinstance(cfg.extra_out_dirs, list):
            for extra_out_dir in cfg.extra_out_dirs:
                shutil.copy(out_path, extra_out_dir)
        else:
            shutil.copy(out_path, cfg.extra_out_dirs)
        if len(cfg.extra_out_dirs) != 0:
            if cfg.debug:
                logging.debug("Copied %s to %s", out_path, cfg.extra_out_dirs)

    if "children" in tree and "output" in tree:
        children: AnyDict | list[AnyDict] = tree["children"]
        if isinstance(children, list):
            with ThreadPoolExecutor() as tpe:
                for i in children:
                    tpe.submit(cfg_tree, cfg, i, storage.copy(), threads)
            threads.append(tpe)
        else:
            thread = Thread(
                target=cfg_tree, args=(cfg, children, storage.copy(), threads)
            )
            thread.start()
            threads.append(thread)
        on_output()
    elif "children" in tree:
        children: AnyDict | list[AnyDict] = tree["children"]
        if isinstance(children, list):
            for i in children:
                cfg_tree(cfg, i, storage.copy(), threads)
        else:
            cfg_tree(cfg, children, storage.copy(), threads)
    elif "output" in tree:
        on_output()
    return threads


def cfg_root(raw_cfg: list[AnyDict] | AnyDict):
    """Process config root."""
    if isinstance(raw_cfg, list):
        for item in raw_cfg:
            executor.submit(cfg_root, item)
        return

    cfg = Config(
        raw_cfg.get("name") or "<unnamed>",
        raw_cfg["src_dir"],
        raw_cfg["out_dir"],
        raw_cfg.get("extra_out_dirs") or [],
        raw_cfg.get("exclude_ext", (".py", ".backup", ".temp")),
        process_excludes(raw_cfg.get("default_excludes", [])),
        raw_cfg.get("debug", True),
        raw_cfg.get("compress", 0),
    )
    tp_start = dt.now()
    logging.info('== Config "%s" ==', cfg.name)
    if raw_cfg.get("clear", True):
        while True:
            try:
                shutil.rmtree(cfg.out_dir)
                break
            except Exception as e:
                logging.exception("Exception when clear output dir:", exc_info=e)
                input("Press enter to try again")

    os.makedirs(cfg.out_dir, exist_ok=True)
    tree: AnyDict | list[AnyDict] = raw_cfg["tree"]
    threads: list[ThreadPoolExecutor | Thread] = []

    if isinstance(tree, list):
        futures: list[Future[list[ThreadPoolExecutor | Thread]]] = []
        for j in tree:
            futures.append(executor.submit(cfg_tree, cfg, j, {}, []))
        for future in as_completed(futures):
            threads.extend(future.result())
    else:
        threads = cfg_tree(cfg, tree, {}, [])
    for threadlike in threads:
        if isinstance(threadlike, ThreadPoolExecutor):
            threadlike.shutdown()
        else:
            threadlike.join()

    logging.info('== Config "%s" == costs %s.', cfg.name, dt.now() - tp_start)


def main():
    """Main function."""
    cfg_path = "config.json"
    log_path = "build.log"
    dir_path = op.dirname(__file__)
    for arg in sys.argv[1:]:
        if arg.startswith("--dir:"):
            dir_path = arg[len("--dir:") :]
        if arg.startswith("--cfg:"):
            cfg_path = arg[len("--cfg:") :]
        if arg.startswith("--log:"):
            log_path = arg[len("--log:") :]

    os.chdir(dir_path)

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

    with open(cfg_path, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    cfg_root(config_data)
    executor.shutdown()

    logging.info("Build stops at %s, total cost %s.", dt.now(), dt.now() - tp_start)


if __name__ == "__main__":
    main()
