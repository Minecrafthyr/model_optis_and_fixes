import zipfile
import os
import shutil

from typing import Union, Optional, List, Tuple, Dict


class zip_temp_dict(Dict[str, bytes]):
    def from_folder(self, folder: str):
        if not os.path.exists(folder) or not os.path.isdir(folder):
            return None
        for root, _, files in os.walk(folder):
            for file in files:
                if os.path.splitext(file)[1] == ".py":
                    continue
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, start=folder)
                try:
                    with open(file_path, "rb") as f:
                        self[relative_path] = f.read()
                except Exception as e:
                    print(f"🚫 Error reading {file_path}: {e}")
        return self


type tree_pack_tuple = Tuple[List[str] | str, str, Optional[tree_pack_list]]
type tree_pack_list = Union[tree_pack_tuple, List[tree_pack_tuple]]



def put_into_zip(
    path: str, target=zip_temp_dict(), remove_if_exists: bool = True
) -> bool:
    if os.path.exists(path):
        if remove_if_exists:
            try:
                os.remove(path)
            except Exception as e:
                print(f"🚫 Error removing {path}: {e}")
                return False
        else:
            print(f"🔒 {path} already exists")
            return False
    try:
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for relative_path, file_content in target.items():
                zipf.writestr(relative_path, file_content)

        print(
            f"✅ {os.path.basename(path)} ({len(target)}📄, {os.stat(path).st_size>>10}Kib)"
        )
        return True
    except Exception as e:
        print(f"🚫 Error creating zip {path}: {e}")
        return False


def zip(
    folder_paths: List[str] | str,
    zip_path: str,
    temp=zip_temp_dict(),
    remove_if_exists: bool = True,
) -> bool:
    if isinstance(folder_paths, str):
        if temp.from_folder(folder_paths) is None:
            print(f"❓ {folder_paths} not found or invalid")
            return False
    else:
        for folder_path in folder_paths:
            if temp.from_folder(folder_paths) is None:
                print(f"❓ {folder_path} not found or invalid")
                return False

    return put_into_zip(zip_path, temp, remove_if_exists)


def ensure_directories_exist(paths: List[str] | str):
    if isinstance(paths, str):
        os.makedirs(paths, exist_ok=True)
    else:
        for path in paths:
            os.makedirs(path, exist_ok=True)


def tree_pack_zip(
    input: tree_pack_tuple,
    input_prefix: str,
    output_prefix: List[str] | str,
    temp=zip_temp_dict(),
):
    path: str | List[str]
    if isinstance(input[0], list):
        path = [(input_prefix + s) for s in input[0]]
    else:
        path = input_prefix + input[0]

    if isinstance(output_prefix, str):
        zip(path, output_prefix + input[1] + ".zip", temp)
    else:
        first_out_path = output_prefix[0] + input[1] + ".zip"
        if zip(path, first_out_path, temp):
            for outprefix in output_prefix[1:]:
                outpath = outprefix + input[1] + ".zip"
                try:
                    shutil.copy(first_out_path, outpath)
                except Exception as e:
                    print(f"📋 🚫 {outpath}: {e}")

    if input[2] is not None:
        tree_pack(input[2], input_prefix, output_prefix, temp)


def tree_pack(
    inputs: tree_pack_list,
    input_prefix: str,
    output_prefix: List[str] | str,
    temp=zip_temp_dict(),
):
    ensure_directories_exist(output_prefix)
    if isinstance(inputs, tuple):
        tree_pack_zip(inputs, input_prefix, output_prefix, temp)
    elif isinstance(inputs, list):
        for input in inputs:
            tree_pack_zip(input, input_prefix, output_prefix, temp)


class tree_pack_input_data(tuple):
    def __new__(
        cls,
        inputs: tree_pack_list,
        input_prefix: str,
        output_prefix: List[str] | str,
    ):
        return super().__new__(cls, (inputs, input_prefix, output_prefix))

    def run(self):
        tree_pack(self[0], self[1], self[2], {})
