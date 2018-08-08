import threading
import time


def work():
    print("子线程%s开始执行" % threading.current_thread().name)
    for n in range(5):
        print("....%d..... " % n)
        time.sleep(1)
    print("子线程%s结束" % threading.current_thread().name)


print("主线程%s开始执行" % threading.current_thread().name)
t = threading.Thread(target=work, name="LOcalhost")  # 指定线程开始执行的函数和子线程的名字，默认名字是Thread-1，Thread-2..
t.start()  # 调用start方法开始执行
t.join()  # 等待所有子线程结束；参数timeout超时时间，设置之后过了这个时间不会等待所有子线程结束就退出了
print("%s主线程结束" % threading.current_thread().name)

