import os


def scan_file(path):
    """第三个遍历目录的方法os.walk()方法"""
    dir_tuple = os.walk(path)  # 返回一个包含三个元素的元组，分别是：路径名、目录列表、文件列表；
    for root_dir, path_list, file_list in dir_tuple:
        for file in file_list:
            print(os.path.join(root_dir, file))


if __name__ == "__main__":
    path = r"D:\pyproject\review"
    scan_file(path)
