import zipfile
import shutil
import json
import logging
import sys
import time
import os


def log_info(s: str):
    logging.info(s)
    print(s)


def log_warning(s: str):
    logging.warning(s)
    print(s)


def log_error(s: str):
    logging.error(s)
    print(s)


def tree_pack_json(data: dict, private: bool):
    tree = data["tree"]
    input_prefix = data["input_prefix"]

    output_prefix = (
        data["output_prefix"]
        if isinstance(data["output_prefix"], list)
        else [data["output_prefix"]]
    )
    
    if private:
        _pop = data.get("private_output_prefix")
        if _pop != None:
            output_prefix.extend(_pop if isinstance(_pop, list) else [_pop])
    storage: dict[str, bytes] = {}
    ignored_ext = tuple(data.get("ignored_ext", [".py", ".backup", ".temp"]))

    def process_path(path: str | dict, storage: dict[str, bytes]) -> int:
        original_cwd = os.getcwd()
        exclude_files = set()
        if isinstance(path, dict):

            def process_exclude_files(items, base_prefix=""):
                for item in items:
                    if isinstance(item, str):
                        path = os.path.normpath(os.path.join(base_prefix, item))
                        exclude_files.add(path.replace(os.sep, "/"))
                    elif isinstance(item, dict):
                        if "prefix" in item and "files" in item:
                            current_prefix = os.path.join(base_prefix, item["prefix"])
                            process_exclude_files(item["files"], current_prefix)
                        elif "files" in item:
                            process_exclude_files(item["files"], base_prefix)

            process_exclude_files(path.get("exclude_files", []))
            path = path["path"]
        try:
            os.chdir(str(input_prefix))
            if os.path.isfile(path):
                with open(path, "rb") as f:
                    storage[os.path.basename(path)] = f.read()
            elif os.path.isdir(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        rpath = os.path.join(root, file)
                        relpath = os.path.relpath(rpath, path)

                        if file.endswith(ignored_ext):
                            logging.debug(f'Ignored "{relpath}"')
                        elif len(exclude_files) != 0:
                            _p = relpath.replace(os.sep, "/")
                            if _p in exclude_files:
                                logging.debug(f'Ignored "{relpath}"')
                                exclude_files.remove(_p)
                        else:
                            with open(rpath, "rb") as f:
                                storage[relpath] = f.read()
            else:
                log_error(f"Path {path} not found!")
        finally:
            os.chdir(original_cwd)
        if len(exclude_files) != 0:
            log_warning(
                f"{len(exclude_files)} files in {path} not excluded: {exclude_files}"
            )

    def process_tree(tree, storage: dict[str, bytes]) -> int:
        if isinstance(tree, list):
            for item in tree:
                process_tree(item, storage.copy())
        elif isinstance(tree, dict):
            inputs = tree["inputs"]
            inputs = inputs if isinstance(inputs, list) else [inputs]
            tp = time.time()
            for path in inputs:
                process_path(path, storage)
            logging.debug(f"Reading cost: {time.time()-tp}s")
            output = f"{tree['output']}.zip" if "output" in tree else None
            if output:
                first_out_path = os.path.join(output_prefix[0], output)
                tp = time.time()
                with zipfile.ZipFile(first_out_path, "w", zipfile.ZIP_STORED) as zipf:
                    for k, v in storage.items():
                        zipf.writestr(k, v)
                logging.debug(f"Zipping cost: {time.time()-tp}s")
                logging.info(
                    f'Success: "{os.path.basename(first_out_path)}" ({len(storage)} files, {os.path.getsize(first_out_path)>>10} KiB)'
                )
                for outprefix in output_prefix[1:]:
                    out_path = os.path.join(outprefix, output)
                    shutil.copy(first_out_path, out_path)
                    logging.debug(f"Successfully copied to {outprefix}.")
                logging.debug(f"Successfully copied to directories.")
            if "children" in tree:
                process_tree(tree["children"], storage)
        else:
            log_error(f"Tree {tree} is not a list or a dict.")

    process_tree(tree, storage)


def load_json_build_cfg(path="config.json", private: bool = False):
    if not os.path.exists(path):
        log_error(f"Config {path} not found!")
        return
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                log_info(f'== Config "{k}" ==')
                tree_pack_json(v, private)


if __name__ == "__main__":
    debug = False
    private = False
    cfgPath = "config.json"
    if "--debug" in sys.argv:
        debug = True
    if "--private" in sys.argv:
        private = True
    for arg in sys.argv[1:]:
        if arg.startswith("--cfgPath:"):
            cfgPath = arg[len("--cfgPath:") :]

    with open("build.log", "w") as f:
        logging.basicConfig(
            stream=f,
            level=logging.DEBUG if debug else logging.INFO,
            format="[%(asctime)s][%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
        )
        log_info(f"Build starts at {time.strftime("%Y-%m-%d, %H:%M:%S")}.")
        load_json_build_cfg(private=private)
        log_info(f"Build stops at {time.strftime("%Y-%m-%d, %H:%M:%S")}.")
