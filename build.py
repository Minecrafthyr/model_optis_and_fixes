import zipfile
import shutil
import json
import logging
import sys
import time
import os
from pathlib import Path
import pathlib

debug = False


def tree_pack_json(data: dict):
    tree = data["tree"]
    input_prefix = Path(data["input_prefix"])
    output_prefix = (
        [Path(p) for p in data["output_prefix"]]
        if isinstance(data["output_prefix"], list)
        else [Path(data["output_prefix"])]
    )
    storage: dict[str, bytes] = {}
    ignored_files = tuple((input_prefix / p) for p in tuple(data.get("ignored_files", [])))
    ignored_ext = tuple(data.get("ignored_ext", [".py", ".backup", ".temp"]))

    def process_path(path: str, storage: dict[str, bytes]):
        if os.path.isfile(path):
            with open(path, "rb") as f:
                storage[os.path.basename(path)] = f.read()
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    rpath = os.path.join(root, file)
                    relpath = os.path.relpath(rpath, path)
                    
                    if (
                        file.endswith(ignored_ext)
                        or Path(rpath) in ignored_files
                    ):
                        logging.debug(f"Ignored {file}")
                        continue
                    with open(rpath, "rb") as f:
                        storage[relpath] = f.read()

    def process_tree(tree, storage: dict[str, bytes]):
        if isinstance(tree, list):
            for item in tree:
                process_tree(item, storage.copy())
        elif isinstance(tree, dict):
            inputs = tree["inputs"]
            inputs = (
                [input_prefix / s for s in inputs]
                if isinstance(inputs, list)
                else [input_prefix / inputs]
            )
            tp = time.time()
            for path in inputs:
                process_path(path, storage)
            logging.debug(f"Reading cost: {time.time()-tp}s")
            output = f"{tree['output']}.zip" if "output" in tree else None
            if output:
                first_out_path = output_prefix[0] / output
                tp = time.time()
                with zipfile.ZipFile(
                    first_out_path.as_posix(), "w", zipfile.ZIP_STORED
                ) as zipf:
                    for k, v in storage.items():
                        zipf.writestr(k, v)
                logging.debug(f"Zipping cost: {time.time()-tp}s")
                logging.info(
                    f'Success: "{first_out_path.name}" ({len(storage)} files, {first_out_path.stat().st_size>>10} KiB)'
                )
                for outprefix in output_prefix[1:]:
                    shutil.copy(first_out_path, outprefix / output)
                    logging.debug(f"Successfully copied to {outprefix}.")
                logging.debug(f"Successfully copied to directories.")
            if "children" in tree:
                process_tree(tree["children"], storage)

    process_tree(tree, storage)


def load_json_build_cfg(path="config.json"):
    path = Path(path)
    if not path.exists():
        logging.error(f'Not found: "{path}"')
        return
    with path.open("r", encoding="utf-8") as f:
        json_data = json.load(f)
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                logging.info(f'== Config "{k}" ==')
                tree_pack_json(v)


if __name__ == "__main__":
    debug = False
    cfgPath = "config.json"
    for arg in sys.argv[1:]:
        if arg.startswith("--debug"):
            debug = True
        elif arg.startswith("--cfgPath:"):
            cfgPath = arg[len("--cfgPath:") :]

    with Path("build.log").open("w") as f:
        logging.basicConfig(
            stream=f,
            level=logging.DEBUG if debug else logging.INFO,
            format="[%(asctime)s][%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        load_json_build_cfg()

# python build.py --debug
