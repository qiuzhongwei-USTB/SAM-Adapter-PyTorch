import os
import random
import shutil

def split_files(input_folder, output_folder_1, output_folder_2, seed=42):
    # 设置随机种子
    random.seed(seed)

    # 获取文件列表
    file_list = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

    # 随机打乱文件列表
    random.shuffle(file_list)

    # 计算分割点
    split_point = int(0.8 * len(file_list))

    # 分割文件
    train_files = file_list[:split_point]
    test_files = file_list[split_point:]

    # 创建输出文件夹
    os.makedirs(output_folder_1, exist_ok=True)
    os.makedirs(output_folder_2, exist_ok=True)

    # 移动文件到不同的输出文件夹
    for file_name in train_files:
        src_path = os.path.join(input_folder, file_name)
        dst_path = os.path.join(output_folder_1, file_name)
        shutil.move(src_path, dst_path)

    for file_name in test_files:
        src_path = os.path.join(input_folder, file_name)
        dst_path = os.path.join(output_folder_2, file_name)
        shutil.move(src_path, dst_path)

# 使用示例
input_folder = '/path/to/input/folder'
output_folder_1 = '/path/to/output/folder1'
output_folder_2 = '/path/to/output/folder2'
split_files(input_folder, output_folder_1, output_folder_2)
