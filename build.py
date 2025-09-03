from dataclasses import dataclass
import datetime
import zipfile
import shutil
import json
import logging
import sys
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


@dataclass
class entry_info:
    src_dir: str
    out_dir: str
    extra_out_dirs: str | list[str]
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


def process_path(
    path: str | dict,
    storage: dict[str, bytes],
    info: entry_info,
):
    original_cwd = os.getcwd()
    exclude: set = set()
    if isinstance(path, dict):
        exclude = process_exclude_files(path.get("exclude", []))
        path = str(path["path"])
    try:
        os.chdir(info.src_dir)
        if os.path.isfile(path):
            with open(path, "rb") as f:
                storage[os.path.basename(path)] = f.read()
        elif os.path.isdir(path):
            files_to_process = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    rpath = os.path.join(root, file)
                    relpath = os.path.relpath(rpath, path)

                    _p = relpath.replace(os.sep, "/")
                    if file.endswith(info.exclude_ext):
                        logging.debug(f'Ignored "{relpath}" by extension')
                    elif _p in exclude:
                        logging.debug(f'Ignored "{relpath}" by relative path')
                        exclude.remove(_p)
                    elif _p in info.default_exclude:
                        logging.debug(f'Ignored "{relpath}" by default')
                    else:
                        files_to_process.append((rpath, relpath))

            # Use multithreading only when there are more than 128 files
            if len(files_to_process) > 128:
                # Thread-safe storage for multithreading
                thread_storage = {}
                lock = threading.Lock()

                def read_file(rpath, relpath):
                    with open(rpath, "rb") as f:
                        content = f.read()
                    with lock:
                        thread_storage[relpath] = content

                with ThreadPoolExecutor() as executor:
                    futures = []
                    for rpath, relpath in files_to_process:
                        futures.append(executor.submit(read_file, rpath, relpath))

                    for future in as_completed(futures):
                        try:
                            future.result()
                        except Exception as e:
                            logging.error(f"Error reading file: {e}")

                # Merge thread storage into main storage
                storage.update(thread_storage)
            else:
                # Original sequential processing for small number of files
                for rpath, relpath in files_to_process:
                    with open(rpath, "rb") as f:
                        storage[relpath] = f.read()
        else:
            logging.error(f"Path {path} not found!")
    finally:
        os.chdir(original_cwd)
    if len(exclude) != 0:
        logging.warning(f"{len(exclude)} files in {path} not excluded: {exclude}")


def process_tree(
    info: entry_info,
    tree: dict | list[dict],
    storage: dict[str, bytes],
):
    if isinstance(tree, list):
        for item in tree:
            process_tree(
                info,
                item,
                storage.copy(),  # Necessary Copy
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
            with zipfile.ZipFile(out_f, "w", zipfile.ZIP_STORED) as zipf:
                for k, v in storage.items():
                    zipf.writestr(k, v)
            if info.debug:
                logging.debug(f"Zipping cost: {time.time()-tp}s")
            logging.info(
                f'Success: "{os.path.basename(out_f)}" \
({len(storage)} files, {os.path.getsize(out_f)>>10} KiB)'
            )
            if isinstance(info.extra_out_dirs, str):
                shutil.copy(out_f, os.path.join(info.extra_out_dirs, out_fn))
            else:
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
    ef = process_exclude_files(
        data.get("default_exclude", []),
    )
    logging.info(f'== Config "{data.get("name") or "<unnamed>"}" ==')
    process_tree(
        info=entry_info(
            data["src_dir"],
            data["out_dir"],
            data.get("extra_out_dirs") or [],
            tuple(data.get("exclude_ext", (".py", ".backup", ".temp"))),
            ef,
            data.get("debug", True),
        ),
        tree=data["tree"],
        storage=dict(),
    )


if __name__ == "__main__":
    cfg_path = "config.json"
    for arg in sys.argv:
        if arg.startswith("--cfg:"):
            cfg_path = arg[len("--cfg:") :]

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

    file_handler = logging.FileHandler("build.log", encoding="utf-8", mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
        )
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    start_time_point = datetime.datetime.now()
    logging.info(f"Build starts at {datetime.datetime.now()}.")
    tree_pack_json(json.load(open(cfg_path)))
    logging.info(
        f"Build stops at {datetime.datetime.now()}, total cost {datetime.datetime.now()-start_time_point}."
    )
