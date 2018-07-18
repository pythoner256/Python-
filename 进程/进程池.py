from multiprocessing import Pool
import time


def worker(num):
    for i in range(10):
        print("num==%d" % num)
        time.sleep(1)


po = Pool(3)  # 创建一个进程池，当前进程池最多创建3个进程
for j in range(5):
    po.apply_async(worker, (j, ))
    """
    向进程池添加任务,如果任务数大于进程池中的进程数，
    不会导致任务添加不进去，会等待进程完成任务之后继续执行
    """
po.close()  # 关闭进程池，不在继续添加任务
po.join()  # 如果没有join会导致进程池中的任务不会执行

