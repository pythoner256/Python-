import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("第" + str(i) + "号" + "线程%s" % self.name)  # name属性中保存的当前线程的名字
            time.sleep(1)


if __name__ == "__main__":
    for j in range(4):
        mt = MyThread()
        mt.start()
