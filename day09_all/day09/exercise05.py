"""
    定义数值累乘的函数
"""


def multiplicative(*args):
    sun = 1
    for number in args:
        sun *= number
    print(sun)

print(multiplicative(1,2,4,5))
