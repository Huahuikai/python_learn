"""
@Name: 01_test
@Author: huahuikai
@Date: 2024/11/8 10:29
@Description: 
"""

# import project02_入门语法.say_hello
# from project02_入门语法 import say_hello
from project02_入门语法 import *
from my_utils import *
def test():
    # project02_入门语法.say_hello.say_hi()
    strings = say_hello.say_hi()
    print(f'这是调用say_hi方法的结果：{strings}')
    reverse_strings = str_util.str_reverse(strings)
    print('这是将say_hi的结果进行反转：' + reverse_strings )

if __name__ == '__main__':
    test()
