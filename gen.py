import zipfile
import os
import shutil

shutil.rmtree('ZippedPacks')
os.mkdir('ZippedPacks')

def zip_multiple_folders(folder_paths, zip_path):
    """
    将多个文件夹的内容压缩成一个ZIP文件。

    :param folder_paths: 要压缩的文件夹路径列表
    :param zip_path: 压缩文件的保存路径（包含文件名和.zip扩展名）
    """
    # 创建一个ZIP文件
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历每个文件夹
        for folder_path in folder_paths:
            # 确保文件夹存在
            if not os.path.exists(folder_path):
                print(f"文件夹 {folder_path} 不存在，将跳过!")
                continue
            
            # 遍历文件夹中的所有文件和子文件夹
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # 获取文件的完整路径
                    file_path = os.path.join(root, file)
                    # 根据相对路径添加文件到ZIP中
                    zipf.write(file_path, os.path.relpath(file_path, start=folder_path))
                    #print(f"已添加文件: {file_path}")

    print(f"所有文件夹的内容已成功压缩到 {zip_path}")

def pack(source, target):
    paths = []
    for s in source:
        paths.append('Assets2\\'+s)

    zip_multiple_folders(paths, f'ZippedPack2\\{target}.zip')


pack(['base'], 'Minecraft Remade Lite')
pack(['base','full'], 'Minecraft Remade')
pack(['base','full','textured'], 'Minecraft Remade Textured')
