from multiprocessing import Process, Queue
import time


def produce(q):
    q.put("a")


def consume(q):
    time.sleep(2)
    result = q.get()
    print(result)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=produce, args=(q, ))
    c = Process(target=consume, args=(q, ))

    p.start()
    c.start()

    p.join()
    c.join()
