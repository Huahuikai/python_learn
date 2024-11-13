"""
@Name: __init__.py
@Author: huahuikai
@Date: 2024/11/12 16:22
@Description: 
"""



from pymysql import Connection

connect = None

def init_db_connection():
    global connect
    if connect is None:
        connect = Connection(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='1234567890',
            autocommit=True,
            database='py_sql'
        )
        print('Database connection initialized')
    return connect


def close_db_connection():
    global connect
    if connect and connect.open:
        connect.close()
        connect = None
        print("Database connection closed.")
