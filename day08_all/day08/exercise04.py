"""
    参照下列代码,定义函数,计算斤量.
        day02/exercise08
    # total_weight = int(input("请输入多少两："))
    # number_jin = total_weight // 16
    # number_liang = total_weight % 16
    # print("结果为：" + str(number_jin) + "斤" + str(number_liang) + "两")
"""


def calculation_weight(total_weight):
    """
    计算斤两
    :param total_weight:
    :return:
    """
    number_jin = total_weight // 16
    number_liang = total_weight % 16
    return number_jin, number_liang


# tuple_result = calculation_weight(100)
# print("结果为：" + str(tuple_result[0]) + "斤" + str(tuple_result[1]) + "两")

jin, liang = calculation_weight(100)
print("结果为：" + str(jin) + "斤" + str(liang) + "两")
