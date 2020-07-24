"""
    参照下列代码,定义函数,计算税率和速算扣除数.
        money = float(input('请输入应纳税所得额'))
        if money <= 36000:
            tax_rate = 0.03
            deduction = 0
        elif money <= 144000:
            tax_rate = 0.1
            deduction = 2520
        elif money <= 300000:
            tax_rate = 0.2
            deduction = 16920
        elif money <= 420000:
            tax_rate = 0.25
            deduction = 31920
        elif money <= 660000:
            tax_rate = 0.3
            deduction = 52920
        elif money <= 960000:
            tax_rate = 0.35
            deduction = 85920
        else:
            tax_rate = 0.45
            deduction = 181920
        # print('税率是%.0f%%速算扣除数是%d' % (tax_rate * 100, deduction))
        print(f'税率是{tax_rate * 100}%速算扣除数是{deduction}')
"""


def get_tax_rate_and_deduction(salary_pay_tax):
    if salary_pay_tax < 36000:
        return 0.03, 0
    if salary_pay_tax <= 144000:
        return 0.1, 2520
    if salary_pay_tax <= 300000:
        return 0.2, 16920
    if salary_pay_tax <= 420000:
        return 0.25, 31920
    if salary_pay_tax <= 660000:
        return 0.3, 52920
    if salary_pay_tax <= 960000:
        return 0.35, 85920
    return 0.45, 181920

# def get_tax_rate_and_deduction(salary_pay_tax):
#     dict_tax_level = {
#         36000: (0.03, 0),
#         144000: (0.1, 2520),
#         300000: (0.2, 16920),
#         420000: (0.25, 31920),
#         660000: (0.3, 52920),
#         960000: (0.35, 85920),
#     }
#     for key, value in dict_tax_level.values():
#         if salary_pay_tax <= key:
#             return value
#     return 0.45, 181920


print(get_tax_rate_and_deduction(1000000))


# def judge_iq(mental_age, real_age):
#     iq = int(mental_age) / int(real_age) * 100
#     if iq >= 140:
#         return "天才"
#     if iq >= 120:
#         return "超常"
#     if iq >= 110:
#         return "聪慧"
#     if iq >= 90:
#         return "正常"
#     if iq >= 80:
#         return "迟钝"
#     return "低能"


# def get_life_stage(age):
#     if age <= 6:
#         return "童年"
#     if age <= 17:
#         return "少年"
#     if age <= 40:
#         return "青年"
#     if age <= 65:
#         return "中年"
#     return "老年"