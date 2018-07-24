from threading import Thread, Lock

num = 0


def test1():
    
    global num
    for i in range(1000000):
        mutex.acquire()  # 上锁
        num += 1
    print(num)
    mutex.release()  # 解锁


def test2():
    
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
    print(num)
    mutex.release()


mutex = Lock()  # 创建互斥锁
th1 = Thread(target=test1)
th2 = Thread(target=test2)
th1.start()
th2.start()



