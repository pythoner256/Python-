import socket


c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个套接字

s_host = 'localhost'
s_port = 50007

c_socket.connect((s_host, s_port))  # 建立连接

data = input("请输入要发送的信息：")
c_socket.send(data)  # 发送信息

info = c_socket.recv(1024)  # 接收信息
print("接收到的数据%s" % info)

c_socket.close()  # 关闭套接字

