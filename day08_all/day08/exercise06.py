"""
    day04/home_work/exercise01
    根据下列代码,定义函数,计算电梯状态.
    num = int(input("请输入电梯承载人数:"))
    weight = float(input("请输入电梯承载重量:"))
    if num <= 10 and weight <= 1000:
        print("电梯正常运行")
    else:
        print("电梯超载")
"""


# def judge_elevator_status(num, weight):
#     if num <= 10 and weight <= 1000:
#         return "正常运行"
#     else:
#         return "电梯超载"

def judge_elevator_status(num, weight):
    """

    :param num:
    :param weight:
    :return:
    """
    return "正常运行" if num <= 10 and weight <= 1000 else"电梯超载"

status = judge_elevator_status(5, 500)
print(status)
