import zipfile
import shutil
import json
import logging
import sys
import time
import os

debug = False


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
            output_prefix.extend(
                _pop
                if isinstance(_pop, list)
                else [_pop]
            )
    storage: dict[str, bytes] = {}
    ignored_files = set()  # 保持为相对路径

    # 处理忽略文件配置
    def process_ignored_files(items, base_prefix=""):
        for item in items:
            if isinstance(item, str):
                path = os.path.normpath(os.path.join(base_prefix, item))
                ignored_files.add(path.replace(os.sep, "/"))
            elif isinstance(item, dict):
                if "prefix" in item and "files" in item:
                    current_prefix = os.path.join(base_prefix, item["prefix"])
                    process_ignored_files(item["files"], current_prefix)
                elif "files" in item:
                    process_ignored_files(item["files"], base_prefix)

    process_ignored_files(data.get("ignored_files", []))

    ignored_ext = tuple(data.get("ignored_ext", [".py", ".backup", ".temp"]))

    def process_path(path: str, storage: dict[str, bytes]):
        original_cwd = os.getcwd()
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

                        if (
                            file.endswith(ignored_ext)
                            or os.path.relpath(rpath).replace(os.sep, "/")
                            in ignored_files
                        ):
                            logging.debug(f'Ignored "{relpath}"')
                            continue
                        with open(rpath, "rb") as f:
                            storage[relpath] = f.read()
            else:
                logging.error(f"Path {path} not found!")
        finally:
            os.chdir(original_cwd)

    def process_tree(tree, storage: dict[str, bytes]):
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

    process_tree(tree, storage)


def load_json_build_cfg(path="config.json", private: bool = False):
    if not os.path.exists(path):
        logging.error(f'Not found: "{path}"')
        return
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                logging.info(f'== Config "{k}" ==')
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
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        load_json_build_cfg(private=private)
