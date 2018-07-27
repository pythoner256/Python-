import socket
from multiprocessing import Process


def deal_with_client(client_socket, client_addr):
    """接收信息"""
    while True:
        data = client_socket.recv(1024)
        if len(data) > 0:  # 信息长度为0，客户端调用close，关闭套接字
            print(">>%s:%s" % (str(client_addr), data))
        else:
            break
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 7878))
    server_socket.listen(5)

    try:
        while True:
            client_socket, client_addr = server_socket.accept()
            client = Process(target=deal_with_client, args=(client_socket, client_addr))
            client.start()
            client_socket.close()

    finally:
        server_socket.close()


if __name__ == "__main__":
    main()

