"""
    day03/exercise09
    根据下列代码,定义函数,计算智商等级.
"""


# mental_age = int(input("心理年龄："))
# real_age = int(input("真实年龄："))
# iq = mental_age / real_age * 100
# if iq >= 140:
#     print("天才")
# elif iq >= 120:  # 小于140
#     print("超常")
# elif iq >= 110:
#     print("聪慧")
# elif iq >= 90:
#     print("正常")
# elif iq >= 80:
#     print("迟钝")
# elif iq < 80:
#     print("低能")

# def judge_iq(mental_age, real_age):
#     """
#         判断IQ
#         :param mental_age: 心理年龄
#         :param real_age: 真实年龄
#         :return: IQ
#     """
#     iq = int(mental_age) / int(real_age) * 100
#     if iq >= 140:
#         return "天才"
#     elif iq >= 120:  # 小于140
#         return "超常"
#     elif iq >= 110:
#         return "聪慧"
#     elif iq >= 90:
#         return "正常"
#     elif iq >= 80:
#         return "迟钝"
#     return "低能"

# return 可以退出函数,不是使用else表达互斥.
def judge_iq(mental_age, real_age):
    """
        判断IQ
        :param mental_age: 心理年龄
        :param real_age: 真实年龄
        :return: IQ
    """
    iq = int(mental_age) / int(real_age) * 100
    if iq >= 140:
        return "天才"
    if iq >= 120:
        return "超常"
    if iq >= 110:
        return "聪慧"
    if iq >= 90:
        return "正常"# 程序执行到本行会退出函数,后续逻辑不在执行.
    if iq >= 80:
        return "迟钝"
    return "低能"


print(judge_iq(26, 26))
