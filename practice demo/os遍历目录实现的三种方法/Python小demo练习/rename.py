import os


path = 'F:\Taylor歌曲\Taylor Swift - Speak Now - World Tour Live'  # 要重命名文件路径
files = os.listdir(path)  # 文件夹下所有的文件
# print(files)
os.chdir(path)  # 将py执行路径修改到操作文件的路径
for file in files:
    pre_name = os.path.splitext(file)[0]  # 获得文件拓展名的前部分名称
    # print(pre_name)
    last_name = os.path.splitext(file)[1]  # 获得文件拓展名
    new_pre_name = pre_name.replace(pre_name[24:26], '')  # 这里把文件的数字替换成空格，也就是删除数字
    f_name = new_pre_name.replace(new_pre_name[0:23], 'Taylor Swift')  # 把文件的前部分替换成想要的名字
    os.rename(file, f_name + last_name)  # 重命名
    """
    因为笔记本有Taylor的歌，但是格式都没有歌手的名字，所以自己写了个脚本修改歌曲名
    """