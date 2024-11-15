"""
@Name: 03_socket编程_服务端开发
@Author: huahuikai
@Date: 2024/11/13 20:14
@Description: 演示Scoket服务端开发
"""

import socket

# socket_server = socket.socket()

with socket.socket() as socket_server:
    socket_server.bind(('localhost', 8888))
    # 监听端口 listen(int) 标识允许连接的数量
    socket_server.listen(1)

    # 返回一个二元元组 元组支持索引！
    # res = socket_server.accept()
    # comment = res[0]
    # address = res[1]
    # 简写：
    # 连接对象 客户端地址信息
    # comment, address = socket_server.accept()
    # 等待连接（阻塞）没有连接就卡在这里 不会往下执行
    with socket_server.accept()[0] as comment:
        # 如果有连接 执行下面的话
        address = socket_server.accept()[1]
        print(f'接收到了客户端请求连接，客户端的信息是：{address}')

        data = comment.recv(1024).decode('UTF-8')
        # recv接收的参数是缓冲区大小 一般是1024
        # recv方法的返回值是一个字节数据也就是bytes对象 不是字符串
        # 通过decode转换为字符串
        print(f'客户端的消息是：{data}')

        # 发送回复消息
        # 通过encode转为字节数据
        msg = input('请输入你要回复的消息：').encode('UTF-8')
        comment.send(msg)

print('连接已经关闭')