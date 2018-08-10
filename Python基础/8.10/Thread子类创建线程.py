from threading import Thread
import time

"""
通过继承Thread子类来完成创建线程，需要重载run方法，实例化一个类对象通过调用start方法去执行run方法
"""


class MyThread(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("子线程开始执行")
        time.sleep(2)
        print("子线程结束")


class MyThread2(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("子线程开始执行")
        time.sleep(2)
        print("子线程结束")


th1 = MyThread("子线程1")
th2 = MyThread('子线程2')

th1.start()
th2.start()

print("主线程结束")

