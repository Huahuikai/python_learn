"""
@Name: 02_装饰器
@Author: huahuikai
@Date: 2024/11/13 19:15
@Description: 
"""

# 在不破坏原函数的基础上 增加新的功能

# 通过装饰器实现在睡眠函数执行前打印对应语句

import time, random


# 先构建一个闭包的外部函数
def outer(f):
    def inner():
        print('我要睡觉了')
        f()
        print('我要起床了')
    return inner

@outer
def sleep():
    times = random.randint(1, 5)
    print(f'{times}秒之后。。。')
    time.sleep(times)




if __name__ == '__main__':
    sleep()
