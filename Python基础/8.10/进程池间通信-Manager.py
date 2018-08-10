from multiprocessing import Pool, Manager
import time


def produce(q):
    q.put("a")


def consume(q):
    time.sleep(2)
    result = q.get()
    print(result)


if __name__ == "__main__":
    q = Manager().Queue()
    p = Pool(2)

    p.apply_async(produce, args=(q, ))
    p.apply_async(consume, args=(q, ))

    p.close()
    p.join()
