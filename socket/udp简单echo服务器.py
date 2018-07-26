import socket


s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建一个udp套接字

s_socket.bind(('', 7788))  # 绑定端口

while True:
    info = s_socket.recvfrom(1024)  # 接收信息;这里返回的是一个元组，第一个元素是信息，第二个是地址信息

    s_socket.sendto(info[0], info[1])  # 将接收到的信息发送回去

s_socket.close()
