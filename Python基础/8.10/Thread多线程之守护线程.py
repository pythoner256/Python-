import time
import threading


def work1():
    print('....1...')
    time.sleep(2)
    print("子线程1结束")


def work2():
    print("....2....")
    time.sleep(3)
    print("子线程2结束")


th1 = threading.Thread(target=work1)
th2 = threading.Thread(target=work2)

# th1.setDaemon(True)
th2.setDaemon(True)  # setDaemon 将线程设置为守护线程，那么主线程结束之后这个线程也会跟着结束

th2.start()
th1.start()

# th1.join()
# th2.join()

print("主线程结束")

