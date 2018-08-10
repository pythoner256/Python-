from multiprocessing import Process, Pipe

"""
pipe适用于指定的两个进城之间的通信，性能较Queue会更高

"""


def producer(pipe):
    pipe.send("a")  # send方法来生成


def consumer(pipe):
    print(pipe.recv())  # recv方法来消费；类似socket


if __name__ == "__main__":
    recevie_pipe, send_pipe = Pipe()

    pro = Process(target=producer, args=(recevie_pipe, ))
    con = Process(target=consumer, args=(send_pipe, ))

    pro.start()
    con.start()

    pro.join()
    con.join()

