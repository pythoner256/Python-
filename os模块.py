
"""一些常用命令"""
# os.remove()  删除文件
#
# os.rename() 重命名文件
#
# os.walk() 生成目录树下的所有文件名
#
# os.chdir() 改变目录
#
# os.mkdir/makedirs 创建目录/多层目录
#
# os.rmdir/removedirs 删除目录/多层目录
#
# os.listdir() 列出指定目录的文件
#
# os.getcwd() 取得当前工作目录
#
# os.chmod() 改变目录权限
#
# os.environ() 获取环境变量；可以通过os.environ.get(key)查看某个环境变量的值
#
# os.path.join() 将分离的各部分组合成一个路径名
#
# os.path.split() 返回( dirname(), basename())元组
#
# os.path.splitext() 返回 (filename, extension) 元组
#
# os.path.getsize() 返回文件大小
#
# os.path.isdir() 是否为目录
#
# os.path.isfile() 是否为文件


# 遍历某个目录下的所有文件
import os


def bian_li(path):
    files = os.listdir(path)  # 获得目录下的所有文件和文件夹
    for file in files:  # 遍历文件和文件夹
        chdir_path = os.path.join(path, file)  # 将文件和文件夹的路径和目录路径结合
        if not os.path.isdir(chdir_path):  # 判断如果不是文件夹就打印文件名字
            print(file)
        else:  # 如果是文件夹就递归继续遍历打印文件夹里的文件
            bian_li(chdir_path)


path = r"C:\Users\Administrator\Desktop\Python复习"
bian_li(path)
