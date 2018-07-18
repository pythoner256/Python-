from multiprocessing import Process
import time


class MyNewProcess(Process):  # 必须继承Process类

    def run(self):  # 重写run方法
        for i in range(5):
            print("子进程开始")
            time.sleep(1)


pro = MyNewProcess()
pro.start()  # 调用start方法就会去调用run方法，不用再写target，子进程执行run函数

for j in range(5):
    print("父进程开始执行")
    time.sleep(1)

