import socket
from threading import Thread


def deal_with_client(client_socket, client_addr):
    while True:
        data = client_socket.recv(1024)
        if len(data) > 0:
            print(">>%s:%s" % (str(client_addr), data))
        else:
            break
    client_socket.close()


def main():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", 7788))
        server_socket.listen(5)
        try:
            while True:
                client_socket, client_addr = server_socket.accept()
                deal_client = Thread(target=deal_with_client, args=(client_socket, client_addr))
                deal_client.start()
        finally:
            server_socket.close()


if __name__ == "__main__":
    main()