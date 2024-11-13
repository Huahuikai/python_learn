"""
@Name: main
@Author: huahuikai
@Date: 2024/11/12 9:35
@Description:   读取数据 通过连接对象调用游标 存入 mysql数据库
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from project05_pymysql import init_db_connection,close_db_connection


def data_count():
    # 文件路径可以从配置或者参数中获取，避免硬编码
    text_file = TextFileReader('assets/一月份数据(test).txt')
    json_file = JsonFileReader('assets/二月份数据(test).txt')

    # 读取文件数据
    jan_data = text_file.read_file()  # 直接返回列表，无需指定类型
    feb_data = json_file.read_file()

    # 合并数据
    all_data: list[Record] = jan_data + feb_data

    connect = init_db_connection()
    try:
        with connect.cursor() as cursor:
            for record in all_data:
                sql = f"insert into py_sql.orders(order_date, order_id, sale, province) " \
                      f"values ('{record.date}','{record.order_id}',{record.sale},'{record.province}')"
                cursor.execute(sql)
    except Exception as e:
        print(e)

    finally:
        connect.close()


def data_print():
    connect = init_db_connection()
    # 读取sql文件并打印
    try:
        with connect.cursor() as cursor:
            sql = 'select * from py_sql.orders'
            cursor.execute(sql)
            res = cursor.fetchall()
            for i in res:
                print(i)

    except Exception as e:
        print(e)

    finally:
        # connect.close()
        close_db_connection()

if __name__ == '__main__':
    # data_count()
    data_print()
