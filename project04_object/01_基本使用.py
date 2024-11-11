"""
@Name: 01_基本使用
@Author: huahuikai
@Date: 2024/11/9 20:44
@Description: 
"""


# 定义一个带有成员方法的类
class Student:
    # 定义成员方法
    def study(self):
        print(f'我叫{self.name},我正在努力学习python')

    def study2(self, msg):
        print(f'我叫{self.name},我正在努力学习{msg}')

    # diy闹铃
    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

    # 构造方法
    def __init__(self, name, age, msg):
        # 可以在这里声明类的属性
        self.name = name
        self.age = age
        print(f'我叫{name},我正在努力学习{msg}')

# 创建一个对象
# huahuikai = Student()
# huahuikai.name = '花会开'
# huahuikai.sex = '男'
# huahuikai.study()
#
# stu = Student()
# stu.name = '花会开'
# stu.sex = '男'
# stu.study2('math')
# stu.ring()

stu2 = Student('花', 20, 'English')
stu2.study()