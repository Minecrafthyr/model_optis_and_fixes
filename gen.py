import zipfile
import os
import shutil

# region functions

type zip_temp_dict = dict[str, bytes]


def put_into(folder: str, target: zip_temp_dict = {}):
    if not os.path.exists(folder) or not os.path.isdir(folder):
        return None
    for root, _, files in os.walk(folder):
        for file in files:
            if os.path.splitext(file)[1] == ".py":
                continue
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=folder)
            with open(file_path, "rb") as f:
                target[relative_path] = f.read()
    return target


def zip(
    folder_paths: list[str] | str,
    zip_path: str,
    temp: zip_temp_dict = {},
    remove_if_exists: bool = True,
):
    if isinstance(folder_paths, str):
        if put_into(folder_paths, temp) is None:
            print(f"{folder_paths} 无效!")
    else:
        for folder_path in folder_paths:
            if put_into(folder_path, temp) is None:
                print(f"{folder_path} 无效!")

    if os.path.exists(zip_path):
        if remove_if_exists:
            os.remove(zip_path)
        else:
            print(f"{zip_path} 已存在, 请删除后重试。")
            return
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for relative_path, file_content in temp.items():
            zipf.writestr(relative_path, file_content)
    print(f"{zip_path} 已压缩完毕。")


type tree_pack_list = tuple[list[str] | str, str, tree_pack_list | None] | list[
    tuple[list[str] | str, str, tree_pack_list | None]
]


def tree_pack_zip(
    input: tuple[list[str] | str, str, tree_pack_list | None],
    input_prefix: str,
    output_prefix: str,
    temp: zip_temp_dict = {},
):
    path: list[str] | str

    if isinstance(input[0], list):
        path = [(input_prefix + s) for s in input[0]]
    else:
        path = input_prefix + input[0]

    zip(
        path,
        output_prefix + input[1] + ".zip",
        temp,
    )
    if input[2] is not None:
        tree_pack(input[2], input_prefix, output_prefix, temp)


def tree_pack(
    inputs: tree_pack_list,
    input_prefix: str,
    output_prefix: str,
    temp: zip_temp_dict = {},
):
    if not os.path.exists(output_prefix):
        os.mkdir(output_prefix)
    if isinstance(inputs, tuple):
        tree_pack_zip(
            inputs,
            input_prefix,
            output_prefix,
            temp,
        )
    elif isinstance(inputs, list):
        for input in inputs:
            tree_pack_zip(
                input,
                input_prefix,
                output_prefix,
                temp,
            )
    else:
        print(f"inputs '{inputs}' must be a tuple or a list")


def copy_files(src_folder: str, dest_folder: str) -> bool:
    if not os.path.exists(src_folder) or not os.path.isdir(src_folder):
        return False
    if not os.path.exists(dest_folder) or not os.path.isdir(dest_folder):
        return False
    for item in os.listdir(src_folder):
        src_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)
        shutil.copy(src_path, dest_path)
    return True


# endregion

tree_pack(
    (
        "Base",
        "Resource Fixes Lite",
        (
            "Full",
            "Resource Fixes",
            (
                "Textured",
                "Resource Fixes Textured",
                (
                    [
                        "Tweak 3D",
                        "Tweak Animation",
                        "Tweak Block States",
                        "Tweak Fire",
                        "Tweak Shadeless Lights",
                        "Tweak Wide Bamboo",
                        "Tweaks",
                    ],
                    "Resource Fixes Extra",
                    None,
                ),
            ),
        ),
    ),
    "Assets/",
    "ZippedPacks/",
)


copy_files(
    "ZippedPacks/", "C:/PCL2/.minecraft/versions/Dev 1.21.5 Fabric/resourcepacks"
)
