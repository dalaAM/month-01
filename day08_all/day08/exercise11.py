"""
    day04/home_work/exercise03
    根据下列代码,定义函数,判断折扣.
"""


# account_type = input("请输入账户类型：")
# money = float(input("请输入消费金额："))
# if account_type == "vip":
#     if money < 500:
#         print("享受85折扣")
#     else:
#         print("享受8折扣")
# else:
#     if money > 800:
#         print("享受9折扣")
#     else:
#         print("原价购买")

# def judge_discount(account_type, money):
#     """
#         判断折扣
#     :param account_type: 账户类型
#     :param money: 消费金额
#     :return: 折扣
#     """
#     if account_type == "vip":
#         return "享受85折扣" if money < 500 else "享受8折扣"
#     else:
#         return "享受9折扣" if money > 800 else "原价购买"
#
# print(judge_discount("vip", 800))


def judge_discount(account_type, money):
    """
        判断折扣
    :param account_type: 账户类型
    :param money: 消费金额
    :return: 折扣
    """
    if account_type == "vip":
        return 0.85 if money < 500 else 0.8
    return 0.9 if money > 800 else 1

# discount = judge_discount("vip", 800)
# print(discount)
print(judge_discount("vip", 800))
