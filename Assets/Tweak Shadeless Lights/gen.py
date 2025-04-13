import os
import json

# 定义目标文件夹路径
folder_path = "D:/Projects/Res Fixes/Assets2/tweak_shadeless_lights/assets"

# 定义 .rpo 文件的内容
rpo_content = {"condition": "!version('luminous-no-shading', '*')"}

# 遍历文件夹中的所有文件
for root, _, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.rpo'):
            continue
        
        with open(os.path.join(root, f"{file_name}.rpo"), 'w') as rpo_file:
            json.dump(rpo_content, rpo_file, indent=4)

print("所有 .rpo 文件已生成。")