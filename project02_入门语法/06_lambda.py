"""
@Name: 06_lambda
@Author: huahuikai
@Date: 2024/11/7 11:22
@Description: 
"""

# lambda表达式
# lambda函数是一种匿名函数，可以把函数作为一个表达式来使用。
# lambda函数的语法格式如下：
# lambda 参数列表: 函数体
# 其中，参数列表是可选的，函数体是lambda表达式的主体，可以是任意有效的Python表达式。

say_hello = lambda name: print("Hello, " + name + "!")

# 使用 lambda 创建匿名函数，函数参数 a、b 与 c 相加，并返回结果：
count_abc = lambda a, b, c: print(a + b + c)


if __name__ == '__main__':
    # say_hello("花会开")
    count_abc(1, 3, 5)