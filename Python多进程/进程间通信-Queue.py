from multiprocessing import Queue, Process


def write(q):
    a_lsit = [i for i in range(10)]
    for j in a_lsit:
        print("正在存入%d" % j)
        q.put(j)
    print("数据存入完毕")


def read(q):
    while True:
        if not q.empty():
            num = q.get()
            print("正在拿出%d" % num)
        else:
            break
    print("数据拿出完毕")


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pw.join()

    pr.start()
    pr.join()

    print("jie shu")