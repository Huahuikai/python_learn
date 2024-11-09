"""
@Name: str_reverse
@Author: huahuikai
@Date: 2024/11/8 14:31
@Description: 
"""


def str_reverse(s):
    # [::-1] 从开头到结尾 反向依次取一个 反向切片 每次向左移动一个
    # print(s[::-1])
    return (s[::-1])

def substr(s,x,y):
    print(s[x:y])

if __name__ == '__main__':
    strings = input('请输入：')
    str_reverse(strings)
    substr(strings,0,3)