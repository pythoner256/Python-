from threading import Thread
import time


def work():
    print("....1.....")
    time.sleep(1)


for i in range(5):
    th = Thread(target=work)
    th.start()
