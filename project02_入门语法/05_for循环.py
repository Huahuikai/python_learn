"""
@Name: 05_for循环
@Author: huahuikai
@Date: 2024/11/7 10:40
@Description: 
"""

def for_test():
    # test_list = [1, 2, 3, 4, 5]
    # 序列类型 下标从0开始 可以设置步长（setup）
    # 但是设置步长一定要有初始值
    test_list = range(0, 10, 2)
    for i in test_list:
        print(i)

#  通过循环输出a的个数
def count_a():
    a_list = ['apple', 'banana', 'orange', 'pear', 'grape']
    count = 0
    for i in a_list:
        if 'a' in i:
            count += 1
    print(f"包含a的单词个数为{count}")


if __name__ == '__main__':
    for_test()
    # count_a()