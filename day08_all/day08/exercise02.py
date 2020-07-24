"""
    定义函数, 将二维列表各元素以表格状打印在终端中
    例如：
        list01 = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
        ]
        1	2	3	4
        5	6	7	8
        9	10	11	12
"""


# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# for line in list01:
#     for item in line:
#         print(item,end = "\t")
#     print()

# 函数命名：动词
def print_double_list(list_target):  # 形式参数
    """

    :param list_target:
    :return:
    """
    for line in list_target:
        for item in line:
            print(item, end="\t")
        print()

# 测试
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print_double_list(list01)  # 实际参数
