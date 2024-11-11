"""
@Name: 02_继承
@Author: huahuikai
@Date: 2024/11/11 14:08
@Description: 
"""


class Phone:
    id = None
    producer = None

    def call_by_4g(self):
        print(f'{self.producer}实现了4G通话')


# 继承
# class 类名(父类名)：
#     类内容体
class Phone2024(Phone):
    face_id = None

    def call_by_5g(self):
        print(f'{self.producer}实现了5G通话')

    def __init__(self, id, producer):
        self.id = id
        self.producer = producer


class RemoteControl(Phone):
    rc_type = '遥控器'

    def control(self):
        print(f'{self.producer}实现了红外遥控器功能')

# 单继承实现
# new_phone = Phone2024(1234321, '华为')
# print(new_phone.id)
# new_phone.call_by_4g()
# new_phone.call_by_5g()

# 定义一个类 继承上面两个类
# class MyPhone(Phone, Phone2024, RemoteControl):#这样的写法会报错 重复继承 会导致解析冲突
# 多继承实现
class MyPhone(Phone2024, RemoteControl):
    pass


my_phone = MyPhone(123321,'华为')
my_phone.call_by_4g()
my_phone.control()

def test():
    import random
    content = random.randint(1,10)
    print(f'随机数是{content}')

def func(data:list):
    return data * 3

if __name__ == '__main__':
    # test()
    print(func([1,2,3]))