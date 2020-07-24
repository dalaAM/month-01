"""
    参照下列代码,定义函数,计算治愈比例.
        day02/exercise06
"""

# confirmed = int(input("请输入确诊人数："))
# cure = int(input("请输入治愈人数："))
# cure_rate = cure / confirmed * 100
# print("治愈比例为" + str(cure_rate) + "%")


def calculate_cure_rate(confirmed, cure):
    """
        计算治愈比率
    :param confirmed:确诊人数
    :param cure:治愈人数
    :return:
    """
    cure_rate = cure / confirmed * 100
    return cure_rate


cure_rate = calculate_cure_rate(300, 150)
print(cure_rate)
