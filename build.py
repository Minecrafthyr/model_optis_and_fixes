from dataclasses import dataclass
import zipfile
import shutil
import json
import logging
import sys
import time
import os

from datetime import datetime as dt


@dataclass
class EntryInfo:
    src_dir: str
    out_dir: str
    extra_out_dirs: list[str]
    exclude_ext: tuple
    default_exclude: set
    debug: bool


def process_exclude_files(
    items: list, exclude_files: set | None = None, base_prefix=""
) -> set:
    if exclude_files is None:
        exclude_files = set()

    for item in items:
        if isinstance(item, str):
            path = os.path.normpath(os.path.join(base_prefix, item))
            exclude_files.add(path.replace(os.sep, "/"))
        elif isinstance(item, dict):
            if "prefix" in item and "files" in item:
                current_prefix = os.path.join(base_prefix, item["prefix"])
                process_exclude_files(item["files"], exclude_files, current_prefix)
            elif "files" in item:
                process_exclude_files(item["files"], exclude_files, base_prefix)
        else:
            logging.warning(f"Invalid exclude item type: {type(item)} - {item}")
    return exclude_files


def try_exclude(relpath: str, info: EntryInfo, exclude: set):
    if relpath.endswith(info.exclude_ext):
        if info.debug:
            logging.debug(f'Ignored "{relpath}" by extension')
        return True
    elif relpath in exclude:
        if info.debug:
            logging.debug(f'Ignored "{relpath}" by relative path')
        exclude.remove(relpath)
        return True
    elif relpath in info.default_exclude:
        if info.debug:
            logging.debug(f'Ignored "{relpath}" by default')
        return True
    else:
        return False


def process_path(
    path: str | dict,
    storage: dict[str, bytes],
    info: EntryInfo,
):
    original_cwd = os.getcwd()
    exclude: set = set()
    zip_mode: bool = True
    if isinstance(path, dict):
        exclude = process_exclude_files(path.get("exclude", []))
        zip_mode = path.get(zip_mode, True)
        path = str(path["path"])
    try:
        os.chdir(info.src_dir)
        if os.path.isfile(path):
            if zip_mode and path.endswith(".zip"):
                with zipfile.ZipFile(file=path, mode="r") as zip:
                    for relpath in zip.namelist():
                        if relpath.endswith("/"):
                            continue
                        if not try_exclude(relpath, info, exclude):
                            storage[relpath] = zip.read(relpath)
            else:
                with open(path, "rb") as f:
                    storage[os.path.basename(path)] = f.read()
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    rpath = os.path.join(root, file)
                    relpath = os.path.relpath(rpath, path).replace(os.sep, "/")
                    if not try_exclude(relpath, info, exclude):
                        with open(rpath, "rb") as f:
                            storage[relpath] = f.read()
        else:
            logging.error(f"Path {path} not found!")
    finally:
        os.chdir(original_cwd)
    if len(exclude) != 0:
        logging.warning(f"{len(exclude)} files in {path} not excluded: {exclude}")


def process_tree(
    info: EntryInfo,
    tree: dict | list[dict],
    storage: dict[str, bytes],
):
    if isinstance(tree, list):
        for item in tree:
            process_tree(
                info,
                item,
                storage.copy() if len(tree) > 1 and len(storage) > 0 else storage,
            )
    elif isinstance(tree, dict):
        inputs = tree["inputs"]
        inputs = list[str](inputs if isinstance(inputs, list) else [inputs])
        if info.debug:
            tp = time.time()
        for path in inputs:
            process_path(path, storage, info)
        if info.debug:
            logging.debug(f"Reading cost: {time.time()-tp}s")
        out_fn = f"{tree['output']}.zip" if "output" in tree else None
        if out_fn:
            out_f = os.path.join(info.out_dir, out_fn)
            if info.debug:
                tp = time.time()
            with zipfile.ZipFile(out_f, "w", zipfile.ZIP_DEFLATED) as zipf:
                for k, v in storage.items():
                    zipf.writestr(k, v)
            if info.debug:
                logging.debug(f"Zipping cost: {time.time()-tp}s")
            logging.info(
                f'Success: "{os.path.basename(out_f)}" ({len(storage)} files, {os.path.getsize(out_f)>>10} KiB)'
            )

            for extra_out_dir in info.extra_out_dirs:
                shutil.copy(out_f, os.path.join(extra_out_dir, out_fn))
        if "children" in tree:
            process_tree(info, tree["children"], storage)
    else:
        logging.error(f"Tree {tree} is not a list or a dict.")


def tree_pack_json(data: list | dict):
    if isinstance(data, list):
        for item in data:
            tree_pack_json(item)
        return
    ef = process_exclude_files(data.get("default_exclude", []))
    logging.info(f'== Config "{data.get("name") or "<unnamed>"}" ==')
    out_dir = data["out_dir"]
    if data.get("clear", True):
        while True:
            try:
                shutil.rmtree(out_dir)
                break
            except Exception as e:
                logging.exception("Exception when clear output dir:", exc_info=e)
                input("Press enter to try again")

    os.makedirs(out_dir, exist_ok=True)
    process_tree(
        info=EntryInfo(
            data["src_dir"],
            out_dir,
            data.get("extra_out_dirs") or [],
            tuple(data.get("exclude_ext", (".py", ".backup", ".temp"))),
            ef,
            data.get("debug", True),
        ),
        tree=data["tree"],
        storage=dict(),
    )


def main():
    cfg_path = "config.json"
    log_path = "build.log"
    dir = os.path.dirname(__file__)
    for arg in sys.argv[1:]:
        if arg.startswith("--dir:"):
            dir = arg[len("--dir:") :]
        if arg.startswith("--cfg:"):
            cfg_path = arg[len("--cfg:") :]
        if arg.startswith("--log:"):
            log_path = arg[len("--log:") :]

    os.chdir(dir)

    # 设置日志配置
    logger = logging.getLogger()
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

    start_time_point = dt.now()
    logging.info(f"Build starts at {dt.now()}.")
    with open(cfg_path, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    tree_pack_json(config_data)
    logging.info(f"Build stops at {dt.now()}, total cost {dt.now()-start_time_point}.")


if __name__ == "__main__":
    main()
