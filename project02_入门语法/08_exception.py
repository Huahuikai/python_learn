"""
@Name: 08_exception
@Author: huahuikai
@Date: 2024/11/7 20:29
@Description: 
"""


#  异常具有传递性

def test_print():
    a = 1 / 0
    print(a)

if __name__ == '__main__':
    try:
        test_print()
    except Exception as e:
        print(f'捕获到的异常是：{e}')