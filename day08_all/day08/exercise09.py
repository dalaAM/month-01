"""
    day04/exercise02
    根据下列代码,定义函数,计算数字的每位相加和.
"""


# number = input("请输入一个数：")  # "1234"
#
# sum = 0
# for item in number:  # "1"               2
#     sum += int(item)  # "1" -> 1       1 + 2
# print("结果是:" + str(sum))

def sum_of_each_number(number):
    """

    :param number:
    :return:
    """
    sum = 0
    for item in str(number):
        sum += int(item)
    return sum


sum = sum_of_each_number(1234)
print("结果是:%d" % (sum))
