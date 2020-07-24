"""
    day04/home_work/exercise04
    根据下列代码,定义函数,计算梯形面积.
    top_base = float(input("请输入上底："))
    bottom_base = float(input("请输入下底："))
    height = float(input("请输入高："))
    result = (top_base + bottom_base) * height / 2
    print("梯形面积是：" + str(result))
"""


def calculate_trapezoidal_area(top_base, bottom_base, height):
    """

    :param top_base:
    :param bottom_base:
    :param height:
    :return:
    """
    return (top_base + bottom_base) * height / 2


area = calculate_trapezoidal_area(5, 8, 4.5)
print("梯形面积是：%s" % area)
# print(f"梯形面积是：{area}")
