from threading import Thread, Lock
import time


class Thread1(Thread):
    def run(self):
        while True:
            if Lock1.acquire():
                print("--线程1--")
                time.sleep(0.5)
                Lock2.release()


class Thread2(Thread):
    def run(self):
        while True:
            if Lock2.acquire():
                print("--线程2--")
                time.sleep(0.5)
                Lock3.release()


class Thread3(Thread):
    def run(self):
        while True:
            if Lock3.acquire():
                print("--线程3--")
                time.sleep(0.5)
                Lock1.release()


Lock1 = Lock()

Lock2 = Lock()
Lock2.acquire()

Lock3 = Lock()
Lock3.acquire()

th1 = Thread1()
th2 = Thread2()
th3 = Thread3()

th1.start()
th2.start()
th3.start()

