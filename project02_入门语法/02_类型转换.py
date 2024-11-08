"""
@Name: 02_类型转换
@Author: huahuikai
@Date: 2024/11/4 20:02
@Description: 
"""
def transation(a):
    b = str(a)
    print(b, type(b))
    c = int(a)
    # 字符串格式化
    print('输出的数字为： %s ' % c, type(c))
    # 多个占位需要用括号包裹
    print('b的值为： %s , c的值为： %s' % (b, c))
    # 对浮点数保四舍五入保留两位小数
    print('a的值四舍五入：%.2f' % a)
    # 格式化快速写法
    print(f'a的值为：{a}')
    print(f'b的值为：{a:.2f}')
    # f-strin字符串格式化可以直接写入表达式
    print(f'1+1的结果：{1+1}')

if __name__ == '__main__':
    transation(3.1415926)
