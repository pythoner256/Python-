import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个tcp套接字

my_host = ''
my_port = 50007

server_socket.bin((my_host, my_port))  # 绑定端口

server_socket.listen(5)  # 监听

while True:
    client_socket, client_addr = server_socket.accept()  # 等待客户端连接;每有一个客户端连接就返回一个客户端套接字
    while True:
        info = client_socket.recv(1024)  # 接收消息
        if len(info) == 0:  # 如果客户端调用close
            break
        client_socket.send(b'Echo=>' + info)  # 发送消息
    client_socket.close()  # 关闭套接字

