from multiprocessing import Process
import time
import os

def work():
    for i in range(3):
        print(".......1111111........子进程%s父进程%s"% (os.getpid(), os.getppid()))
        time.sleep(0.5)

def work1():
    for i in range(3):
        print(".......2222222........子进程%s父进程%s"% ( os.getpid(), os.getppid()))
        time.sleep(0.5)


if __name__ == "__main__":
    p1 = Process(target=work)
    p2 = Process(target=work1)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("子进程%s"% (p1.name))
    print("子进程%s"% (p2.name))
    for i in range(100):
        print(i)


"""
join方法会等子进程结束之后才执行父进程；如果没有调用这个方法会先去执行父进程然后进入子进程
"""