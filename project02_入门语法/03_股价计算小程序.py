"""
@Name: 03_股价计算小程序
@Author: huahuikai
@Date: 2024/11/5 10:03
@Description: 基础语法练习
"""

name = "huahuikai"
stock_price = 100.5
# 股票代码 (数字不能以0开头)
stock_code = "000001"
# 每日增长系数
stock_price_daily_growth_factor = 1.2
growth_days = 5

# 计算股价
def print_info():
    print(f'公司：{name},股票代码：{stock_code},当前股价：{stock_price}')
    print('每日增长系数：%.1f ,增长天数：%d,股价达到了: %.2f' % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** growth_days))
    x = input('请输入a键')
    print(x)

if __name__ == '__main__':
    print_info()