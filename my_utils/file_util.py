"""
@Name: file_utils
@Author: huahuikai
@Date: 2024/11/8 14:32
@Description: 
"""

def print_file_info():
    try:
        f = open('F:/a.txt','r',encoding='UTF-8')
        print(f.read())
        f.close()
    except Exception as e:
        print(f'报错了：{e}')

def print_file_info2():
    try:
        with open('F:/a.txt','r',encoding='UTF-8') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f'报错了：{e}')

def append_file(file_name,data):
    f = open(file_name,'a',encoding='UTF-8')
    f.write(data)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    # print_file_info()
    # print_file_info2()
    append_file('a.txt','hello world')