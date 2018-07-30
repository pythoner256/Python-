import os


def scan_file(path):
    """第二个遍历目录的方法os.isfile()方法"""
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            print(file_path)
        else:
            scan_file(file_path)


if __name__ == '__main__':
    path = r"D:\pyproject\review"
    scan_file(path)

