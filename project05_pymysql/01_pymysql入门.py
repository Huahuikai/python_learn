"""
@Name: 01_pymysql入门
@Author: huahuikai
@Date: 2024/11/12 16:23
@Description: 
"""
from pymysql import Connection

connect = Connection(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234567890',
    autocommit=True  # 设置自动提交 就不需要手动提交了
)

# 获取mysql版本信息
# print(connect.get_server_info())

connect.select_db('bigdata3221')
curso = connect.cursor()
# curso.execute('select * from student')
# content = curso.fetchall()
# print(content)
curso.execute("insert into student values(5,'小红',22,'女')")
# 数据的插入 需要 连接对象.commit()进行确认
# connect.commit()

# 关闭连接
connect.close()