"""
@Name: main
@Author: huahuikai
@Date: 2024/11/12 9:35
@Description: 
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
import pyecharts
from pyecharts.options import TitleOpts
from collections import defaultdict

def data_count():
    # 文件路径可以从配置或者参数中获取，避免硬编码
    text_file = TextFileReader('assets/一月份数据(test).txt')
    json_file = JsonFileReader('assets/二月份数据(test).txt')

    # 读取文件数据
    jan_data = text_file.read_file()  # 直接返回列表，无需指定类型
    feb_data = json_file.read_file()

    # 合并数据
    all_data = jan_data + feb_data

    # 使用 defaultdict 来简化数据统计
    data_dict = defaultdict(int)
    for record in all_data:
        data_dict[record.date] += record.sale

    print(dict(data_dict))  # 将 defaultdict 转换为普通字典打印
    return dict(data_dict)  # 返回普通字典而不是 defaultdict


def view():
    # 获取数据
    data_dict = data_count()

    # 使用 pyecharts 生成图表
    bar = pyecharts.charts.Bar()
    bar.add_xaxis(list(data_dict.keys()))
    bar.add_yaxis("销售额", list(data_dict.values()))  # 用中文更友好
    bar.set_global_opts(
        title_opts=TitleOpts(title='每日销售额')
    )
    bar.render('每日销售额图表.html')


if __name__ == '__main__':
    # 直接调用 view() 来生成图表
    view()
