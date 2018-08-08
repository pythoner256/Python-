from threading import Thread
import time
"""多线程共享全局变量"""

num = 100


def func1():
    global num
    for i in range(3):
        num += 1
    print(num)


def func2():
    global num
    print(num)


th = Thread(target=func1)
th.start()  # num=103
time.sleep(1)

th2 = Thread(target=func2)
th2.start()  # num=103

