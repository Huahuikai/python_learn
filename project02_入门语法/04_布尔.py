"""
@Name: 04_布尔
@Author: huahuikai
@Date: 2024/11/5 14:02
@Description: 循环计算
"""
def is_adult():
    while True:
        # input 输入的是·字符串·，需要用 int() 转换为整数
        age = int(input("请输入你的年龄："))
        if age >= 18:
            print("你已经成年了")
        elif age >= 16:
            print("你快成年了")
        else:
            print("你太小了，还未成年")

def guess_number():
    import random
    # randint 随机生成一个整数
    number = random.randint(1, 10)
    count = 0
    # print(number)
    while True:
        input_number = int(input('请输入一个数字：'))
        count += 1
        print(f'第{count}次猜测的结果：')
        if input_number == number:
            print(f'恭喜你猜对了！数字是{number},你用了{count}次猜测')
            break
        elif input_number < number:
            print('你猜的数字小了')
        else:
            print('你猜的数字大了')

def guess_number2():
        import random
        # randint 随机生成一个整数
        number = random.randint(1, 10)
        count = 0

        while True:
            input_number = int(input('请输入一个数字：'))
            count += 1
            print(f'第{count}次猜测的结果：')

            if input_number == number:
                print(f'恭喜你猜对了！数字是{number},你用了{count}次猜测')
                break
            else:
                print('你猜的数字' + ('小了' if input_number < number else '大了'))

# while 循环打印九九乘法表
def print_cfb():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f'{i}*{j}={i*j}', end='\t')
            j += 1
        print()
        i += 1

if __name__ == '__main__':
    # is_adult()
    # guess_number()
    # guess_number2()
    print_cfb()