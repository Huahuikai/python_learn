"""
@Name: 01_闭包操作
@Author: huahuikai
@Date: 2024/11/13 16:38
@Description: 闭包练习
"""

# 简单闭包练习：
def out_func(log):
    def inner_func(msg):
        print(f'<{log}> {msg} <{log}>')

    return inner_func


if __name__ == '__main__':
    # 外层方法返回的是一个函数 然后进行内部函数的传参
    func1 = out_func('湖南科技职业学院')
    func1('huahuikai')
