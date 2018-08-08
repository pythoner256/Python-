from multiprocessing import Manager, Pool
import time
import os


def write(q):
    print("进程%s开始执行" % os.getpid())
    for i in range(10):
        q.put(i)
        print("正在存入%d" % i)
    print(q.qsize())
    time.sleep(3)


def read(q):
    print("进程%s开始执行" % os.getpid())
    while True:
        if not q.empty():
            num = q.get()
            print("正在获取%s" % num)
        else:
            break


if __name__ == "__main__":
    start = time.time()
    q = Manager().Queue()
    pool = Pool()
    # pool.apply_async(write, args=(q, ))
    # pool.apply_async(read, args=(q, ))
    pool.apply(write, args=(q, ))
    pool.apply(read, args=(q, ))
    pool.close()
    pool.join()

    print("程序执行完成")
    stop = time.time()
    t = stop - start
    print(t)