from multiprocessing import Process
import time


def test():
    for i in range(5):
        print("*"*10)
        time.sleep(1)


p = Process(target=test)  # 实例化一个对象就是创建一个子进程，指定target就是让子进程去执行的代码
p.start()  # 调用start方法子进程才开始执行；当目标函数执行完之后子进程就结束
p.join()  # 阻塞(等待某个条件的发生，如果这个条件没有发生就一直停在这) 等到所有的子进程结束了才会继续往下执行

print("jie shu")

