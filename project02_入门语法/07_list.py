"""
@Name: 07_list
@Author: huahuikai
@Date: 2024/11/7 14:28
@Description: 
"""


def get_index():
    test_list = ['hello', 'world', 'hua']
    hua_index = test_list.index('hua')
    print(f'元素"hua"的索引为：{hua_index}')
    # 元素不存在
    # print(test_list.index('huahuikai'))
    # 通过下标修改值
    test_list[2] = 'huahuikai'
    print(f'修改后的列表为：{test_list}')
    # 在尾部增加元素
    test_list.append('tail_element')
    print(f'在尾部新增元素：{test_list}')
    # 还可以通过extend追加整个列表
    test_list2 = ['a', 'b', 'c']
    test_list.extend(test_list2)
    print(f'在尾部新增一个新的列表：{test_list}')
    # 删除元素
    test_list3 = ['a', 'b', 'c']
    del test_list3[1]
    print(test_list3)
    pop_element = test_list3.pop(1)
    print(f'删除的元素是：{pop_element}')


if __name__ == '__main__':
    get_index()
