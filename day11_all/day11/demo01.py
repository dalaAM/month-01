"""
    类成员:通过类名xx
        类变量
        类方法
    exercise:exercise01 02
"""

class ICBC:
    # 类变量:大家的钱
    total_money = 1000000

    # 类方法:操作类变量
    @classmethod
    def print_total_money(cls):
        # print("总行的钱:%d" % ICBC.total_money)
        print("总行的钱:%d" % cls.total_money)  # cls 就是 类名(ICBC)

    def __init__(self, name, money):
        # 实例变量:自己的钱
        self.name = name
        self.money = money
        # 创建支行时,总行钱减少
        ICBC.total_money -= money


trt = ICBC("陶然亭支行", 200000)
trt.money += 900000
print("陶然亭支行的钱增加%d" % trt.money)
# print("总行的钱:%d" % ICBC.total_money) # 类名访问类变量
# print("总行的钱:%d" % trt.total_money) # 不建议:对象地址访问类变量
# 类名访问类方法
ICBC.print_total_money()

tt = ICBC("天坛支行", 300000)
print("天坛支行的钱%d" % tt.money)
print("总行的钱:%d" % ICBC.total_money)
# print("总行的钱:%d" % tt.total_money)
