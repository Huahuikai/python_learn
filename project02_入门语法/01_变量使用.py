"""
@Name: 01_变量使用
@Author: huahuikai
@Date: 2024/11/4 16:05
@Description: 
"""

# 变量的定义
# 变量名只能包含字母、数字和下划线，且不能以数字开头
# 变量名区分大小写
money = '1000'
print('我的余额为：' + money)
# 花费了100元
money2 = int(money) - 100
print('剩余的余额为：' + str(money2))
