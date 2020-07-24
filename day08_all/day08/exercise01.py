"""
    定义函数, 在一行中打印一维列表各元素
    例如：
        list01 = [2,3,4,56]
        list02 = ["a","b","c","d"]

        2 3 4 56
        a b c d
"""


# list01 = [2, 3, 4, 56]
# list02 = ["a", "b", "c", "d"]
#
# for item in list01:
#     print(item,end = " ")
# print()
#
# for item in list02:
#     print(item,end = " ")
# print()

def print_single_list(list_target):
    """
        打印一维列表
    :param list_target:需要打印的一维列表
    :return:
    """
    for item in list_target:
        print(item, end=" ")
    print()


# 测试...
list01 = [2, 3, 4, 56]
print_single_list(list01) # list_target　= list01
print_single_list(["a", "b", "c", "d"]) # list_target　= ["a", "b", "c", "d"]
