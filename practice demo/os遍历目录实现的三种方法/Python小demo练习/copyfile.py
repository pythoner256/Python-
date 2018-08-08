# -*- coding:utf-8 -*-
# 1.得到要复制的文件夹名字
# 2.创建一个新的文件夹
# 3.打开文件得到所有的文件名字
from multiprocessing import Pool, Manager
import os


def copy(name, folder_name, new_folder_name, queue):
    fr = open(folder_name+'/'+name)
    fw = open(new_folder_name+'/'+name, 'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put()


def main():
    folder_name = input("请输入要复制的文件夹的名称：")
    new_folder_name = folder_name+'复件'  # 命名新的文件夹名称
    os.mkdir(new_folder_name)  # 创建新的文件夹
    filename = os.listdir(folder_name)  # 获取要复制的文件夹里的文件名

    pool = Pool(5)  # 创建进程池
    queue = Manager().Queue()  # 创建队列
    for name in filename:
        pool.apply_async(copy, args=(name, folder_name, new_folder_name, queue))
    num = 0
    all_num = len(filename)
    while True:
        queue.get()
        num += 1
        copy_rate = num/all_num
        print('\r复制进度是：%0.2f%%' % (copy_rate*100), end='')
        if num == all_num:
            break

    print('\n已完成复制')


if __name__ == "__main":
    main()
