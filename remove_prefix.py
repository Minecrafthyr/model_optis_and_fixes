import os

def remove_prefix(directory, prefix):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查是否以指定前缀开头
        if filename.startswith(prefix):
            # 生成新的文件名，移除前缀
            new_filename = filename[len(prefix):]
            # 生成完整的文件路径
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed: "{filename}" to "{new_filename}"')

remove_prefix(os.path.split(__file__)[0], 'soul_fire_')