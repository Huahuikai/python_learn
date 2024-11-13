"""
@Name: data_define
@Author: huahuikai
@Date: 2024/11/11 16:01
@Description: 
"""


# 封装一个类接收数据
class Record:

    def __init__(self, date, order_id, sale, province):
        self.date = date
        self.order_id = order_id
        self.sale = sale
        self.province = province
    # 打印对象 或者 使用 str方法时会自动将对象转换为字符串的格式
    # 次数定义在Record类里面 输出实例时使用
    def __str__(self):
        return f"{self.date},{self.order_id},{self.sale},{self.province}"

