import zipfile
import os
import shutil


def put_into(folder: str, target: dict[str, str] = {}):
    if not os.path.exists(folder) and not os.path.isdir(folder):
        return None
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=folder)
            with open(file_path, "rb") as f:
                target[relative_path] = f.read()
    return target


def multizip(folder_paths: list[str], zip_path: str, temp: dict[str, str] = {}):
    for folder_path in folder_paths:
        if put_into(folder_path, temp) is None:
            print(f"{folder_path}无效!")
            continue
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for relative_path, file_content in temp.items():
            zipf.writestr(relative_path, file_content)
    print(f"所有文件夹的内容已成功压缩到 {zip_path}")


def multizips(inputs: list[tuple[list[str], str]]):
    temp: dict = {}
    for input in inputs:
        multizip(input[0], input[1], temp)


def multipack(source, target):
    multizip([os.path.join("Assets2", s) for s in source], f"ZippedPacks\\{target}.zip")


def multipacks(inputs: list[tuple[list[str], str]]):
    temp: dict = {}
    for input in inputs:
        multizip(
            [os.path.join("Assets2", s) for s in input[0]],
            f"ZippedPacks\\{input[1]}.zip",
            temp,
        )


if os.path.exists("ZippedPacks"):
    shutil.rmtree("ZippedPacks")
os.mkdir("ZippedPacks")

# pack(["base"], "Resource Fixes Lite")
# pack(["base", "full"], "Resource Fixes")
# pack(["base", "full", "textured"], "Resource Fixes Textured")
# pack(
#    [
#        "base",
#        "full",
#        "textured",
#        "tweaks",
#        "tweak_3d",
#        "tweak_animation",
#        "tweak_fire",
#        "tweak_shadeless_lights",
#        "tweak_wide_bamboo",
#    ],
#    "Resource Fixes Extra",
# )

multipacks(
    [
        (["base"], "Resource Fixes Lite"),
        (["full"], "Resource Fixes"),
        (["textured"], "Resource Fixes Textured"),
        (
            [
                "tweaks",
                "tweak_3d",
                "tweak_animation",
                "tweak_fire",
                "tweak_shadeless_lights",
                "tweak_wide_bamboo",
            ],
            "Resource Fixes Extra",
        ),
    ]
)
