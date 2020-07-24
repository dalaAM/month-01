'''
    函数 -- 调用过程
'''
# ------------------定义函数------------------
def repeated_attacks(count):  # -----------(2)
    """
        重复攻击的做法
    :param count: int类型,重复的次数
    :return:
    """
    for number in range(count):
        single_attack()

def single_attack():          # -----------(3)
    """
        单次攻击的做法 x  1次
    :return:
    """
    print("临门一脚")
    print("直拳")
    print("摆拳")
    print("勾拳")

# ------------------调用函数------------------
repeated_attacks(3)    # -----------(1)

