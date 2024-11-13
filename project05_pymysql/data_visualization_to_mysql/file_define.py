"""
@Name: file_define
@Author: huahuikai
@Date: 2024/11/11 16:05
@Description: 
"""
import json

from data_define import Record


# 先定义一个抽象类 具体实现方法 在子类中实现
class FileReader:
    def read_file(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    # 定义子类的成员变量
    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Record]:
        with open(self.path, 'r', encoding='GB2312') as f:
            record_list = []
            for i in f.readlines():
                i = i.strip()
                data_list = i.split(',')
                # 列表添加方法：append()
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                record_list.append(record)
            return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Record]:
        with open(self.path, 'r', encoding='GB2312') as f:
            record_list = []
            for i in f.readlines():
                # 通过json.loads 将json字符串转换为python数据格式(字典)
                data_dict = json.loads(i)
                record = Record(data_dict["date"], data_dict["order_id"], data_dict["sale"], data_dict['province'])
                record_list.append(record)
        return record_list


if __name__ == '__main__':
    file1 = TextFileReader('assets/一月份数据(test).txt')
    list1 = file1.read_file()

    # test
    # with open('./assets/一月份数据(test).txt','r') as f:
    #     print(type(f.read()))

    file2 = JsonFileReader('assets/二月份数据(test).txt')
    list2 = file2.read_file()

    for i in list1:
        print(i)

    for i in list2:
        print(i)
