import multiprocessing
import time


def work(num):
    print(num)
    time.sleep(2)
    return num


if __name__ == "__main__":
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.apply_async(work, args=(10, ))
    pool.apply(work, args=(10, ))  # apply 是阻塞式添加任务,如果自定义最多有3个进程，而任务数有10个，此时会先等待3个任务都完成之后才添加新任务

    con = pool.apply_async(work, args=(10, ))
    print(con.get())  # 通过get方法获取返回的值

    result = pool.map(work, [1, 5, 3])
    for i in result:
        print(i)

    pool.close()
    pool.join()  # 调用join方法之前必须要调用close方法；关闭进程池，不再接收新任务
    print("主进程结束")

