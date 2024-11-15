"""
@Name: 04_socket客户端
@Author: huahuikai
@Date: 2024/11/15 10:33
@Description: 
"""

import socket

# 创建客户端 socket
with socket.socket() as client_socket:
    client_socket.connect(('localhost', 8888))  # 连接到服务器
    print("连接到服务器成功！")

    # 发送消息到服务器
    message = "Hello, server!"
    client_socket.send(message.encode('UTF-8'))

    # 接收服务器的回复
    data = client_socket.recv(1024).decode('UTF-8')
    print(f"收到服务器回复：{data}")
