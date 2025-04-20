import zipfile
import os
import shutil

from typing import Optional, List, Tuple, Dict


class zip_temp_dict(Dict[str, bytes]):
    def load_from_folder(self, folder: str):
        if os.path.isdir(folder):
            for root, _, files in os.walk(folder):
                for file in files:
                    if not file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, "rb") as f:
                                self[os.path.relpath(file_path, folder)] = f.read()
                        except Exception as e:
                            print(f"🚫 {file_path}: Error {e}")
        return self


type tree_pack_tuple = Tuple[List[str] | str, str, Optional[tree_pack_list]]
type tree_pack_list = tree_pack_tuple | List[tree_pack_tuple]


def put_into_zip(
    path: str, target=zip_temp_dict()
 ) -> bool:
    try:
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for k, v in target.items():
                zipf.writestr(k, v)
        print(
            f"✅ {os.path.basename(path)} ({len(target)}📄, {os.stat(path).st_size>>10}Kib)",
            end="",
            flush=True,
        )
        return True
    except Exception as e:
        print(f"🚫 {path}: Error {e}")
        return False

def zip(
    folder_paths: List[str] | str,
    zip_path: str,
    temp=zip_temp_dict(),
    remove_if_exists: bool = True,
) -> bool:
    if isinstance(folder_paths, str):
        if temp.load_from_folder(folder_paths) is None:
            print(f"❓ {folder_paths}: not found or invalid")
            return False
    else:
        for folder_path in folder_paths:
            if temp.load_from_folder(folder_path) is None:
                print(f"❓ {folder_path}: not found or invalid")
                return False
    if os.path.exists(zip_path):
        if remove_if_exists:
            try:
                os.remove(zip_path)
            except Exception as e:
                print(f"🚫 {zip_path}: Error {e}")
                return False
        else:
            print(f"🔒 {zip_path}: already exists")
            return False
    return put_into_zip(zip_path, temp)


def tree_pack_zip(
    input: tree_pack_tuple,
    input_prefix: str,
    output_prefix: List[str] | str,
    temp=zip_temp_dict(),
):
    paths: str | List[str]
    if isinstance(input[0], list):
        paths = [(input_prefix + s) for s in input[0]]
        for path in paths:
            os.makedirs(path, exist_ok=True)
    else:
        paths = input_prefix + input[0]
        os.makedirs(paths, exist_ok=True)

    if isinstance(output_prefix, str):
        zip(paths, output_prefix + input[1] + ".zip", temp)
        print()
    else:
        first_out_path = output_prefix[0] + input[1] + ".zip"
        if zip(paths, first_out_path, temp):
            for outprefix in output_prefix[1:]:
                outpath = outprefix + input[1] + ".zip"
                try:
                    shutil.copy(first_out_path, outpath)
                    print("📋 ", end="", flush=True)
                except Exception as e:
                    print(f"📋 🚫 {outpath}: {e}")
        print()

    if input[2] is not None:
        tree_pack(input[2], input_prefix, output_prefix, temp)


def tree_pack(
    inputs: tree_pack_list,
    input_prefix: str,
    output_prefix: List[str] | str,
    temp=zip_temp_dict(),
):
    if isinstance(inputs, tuple):
        tree_pack_zip(inputs, input_prefix, output_prefix, temp)
    elif isinstance(inputs, list):
        for input in inputs:
            tree_pack_zip(input, input_prefix, output_prefix, temp)


class tree_pack_input_data(tuple):
    inputs: tree_pack_list
    input_prefix: str
    output_prefix: List[str] | str
    def __new__(cls, inputs: tree_pack_list, input_prefix: str, output_prefix: List[str] | str):
        return super().__new__(cls, (inputs, input_prefix, output_prefix))
    def __init__(self, inputs: tree_pack_list, input_prefix: str, output_prefix: List[str] | str):
        self.inputs = inputs
        self.input_prefix = input_prefix
        self.output_prefix = output_prefix
    def run(self):
        print()
        tree_pack(self[0], self[1], self[2], zip_temp_dict())
