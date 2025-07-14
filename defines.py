from dataclasses import dataclass
import zipfile
import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from typing import Optional, List, Tuple, Dict


class zip_temp_dict(Dict[str, bytes]):
    def load(self, folder: str):
        """
        加载文件夹或文件内容到字典，键为相对路径，值为二进制内容。
        忽略 .py、.backup、.temp 文件。
        """
        if os.path.isfile(folder):
            with open(folder, "rb") as f:
                self[os.path.basename(folder)] = f.read()
        elif os.path.isdir(folder):
            file_tasks = []
            for root, _, files in os.walk(folder):
                for file in files:
                    if not file.endswith((".py", ".backup", ".temp")):
                        file_path = os.path.join(root, file)
                        file_tasks.append(file_path)
            lock = threading.Lock()

            def read_file(file_path):
                try:
                    with open(file_path, "rb") as f:
                        rel_path = os.path.relpath(file_path, folder)
                        return rel_path, f.read()
                except Exception as e:
                    print(f"[Fail] {file_path}: Error {e}")
                    return None

            with ThreadPoolExecutor(max_workers=8) as executor:
                for future in as_completed(
                    [executor.submit(read_file, fp) for fp in file_tasks]
                ):
                    result = future.result()
                    if result:
                        rel_path, content = result
                        with lock:
                            self[rel_path] = content
        return self


def put_into_zip(path: str, target: Optional[zip_temp_dict] = None) -> bool:
    """
    将 zip_temp_dict 内容写入 zip 文件。
    """
    if target is None:
        target = zip_temp_dict()
    try:
        with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as zipf:
            for k, v in target.items():
                zipf.writestr(k, v)
        print(
            f"[OK] {os.path.basename(path)} ({len(target)} files, {os.stat(path).st_size>>10}Kib)",
            end="",
            flush=True,
        )
        return True
    except Exception as e:
        print(f"[Fail] {path}: Error {e}")
        return False


def zip(
    folder_paths: List[str] | str,
    zip_path: str,
    temp: Optional[zip_temp_dict] = None,
    remove_if_exists: bool = True,
) -> bool:
    """
    将文件夹或文件压缩为 zip。
    """
    if temp is None:
        temp = zip_temp_dict()
    if isinstance(folder_paths, str):
        if temp.load(folder_paths) is None:
            print(f"[Fail] {folder_paths}: not found or invalid")
            return False
    else:
        for folder_path in folder_paths:
            if temp.load(folder_path) is None:
                print(f"[?] {folder_path}: not found or invalid")
                return False
    if os.path.exists(zip_path):
        if remove_if_exists:
            try:
                os.remove(zip_path)
            except Exception as e:
                print(f"[?] {zip_path}: Error {e}")
                return False
        else:
            print(f"[Lock] {zip_path}: already exists")
            return False
    return put_into_zip(zip_path, temp)


type tree_pack_tuple = Tuple[List[str] | str, str, Optional[tree_pack_list]]
type tree_pack_list = tree_pack_tuple | List[tree_pack_tuple]


def tree_pack_zip(
    input: tree_pack_tuple,
    input_prefix: str,
    output_prefix: List[str] | str,
    temp=zip_temp_dict(),
):
    paths = (
        [os.path.join(input_prefix, s) for s in input[0]]
        if isinstance(input[0], list)
        else [os.path.join(input_prefix, input[0])]
    )

    for path in paths:
        if os.path.isfile(path) or os.path.isdir(path):
            temp.load(path)
    if input[1] is not None:
        if isinstance(output_prefix, str):
            zip(paths, os.path.join(output_prefix, input[1] + ".zip"), temp)
            print()
        else:
            first_out_path = os.path.join(output_prefix[0], input[1] + ".zip")
            if zip(paths, first_out_path, temp):
                for outprefix in output_prefix[1:]:
                    outpath = os.path.join(outprefix, input[1] + ".zip")
                    try:
                        shutil.copy(first_out_path, outpath)
                        print("[C]", end="", flush=True)
                    except Exception as e:
                        print(f"[Copy Failed] {outpath}: {e}")
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
            tree_pack_zip(input, input_prefix, output_prefix, zip_temp_dict(temp.copy()))

@dataclass
class tree_pack_input_data:
    inputs: tree_pack_list
    input_prefix: str
    output_prefix: List[str] | str

    def run(self):
        print()
        tree_pack(self.inputs, self.input_prefix, self.output_prefix, zip_temp_dict())
