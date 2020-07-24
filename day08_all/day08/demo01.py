'''
    函数 -- 功能
        价值1:减少代码的重复
        *制作
            def 函数名称(参数):
                """
                    文档字符串
                """
                函数体
        调用
'''

# 调用(使用)函数
print("你好,世界!")
result = list("你好,世界!")
print(result)  # ['你', '好', ',', '世', '界', '!']

# 为什么要制作功能?
# 因为之前都是做法+使用,当做法变化时,会修改多次.
"""
# 做法 + 使用
print("直拳")
print("摆拳")
print("勾拳")

# ...... 此处省略100行代码

# 做法 + 使用
print("直拳")
print("摆拳")
print("勾拳")
"""


# 解决:做法1次,使用多次.当变化时只修改1次
# 重命名快捷键:shift+f6
# 在函数调用语句上:ctrl + 鼠标左键,可以调到函数定义的语句
def single_attack():
    """
        单次攻击的做法 x  1次
    :return:
    """
    print("直拳")
    print("摆拳")
    print("勾拳")


# 使用 x 2次
single_attack()
single_attack()


# 参数:调用函数时  给 制作函数时 传递的信息
# 形式参数:表面的/虚拟的/抽象的 变量
# 价值:让数据灵活
def repeated_attacks(count):
    """
        重复攻击的做法
    :param count: int类型,重复的次数
    :return:
    """
    for number in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")


# 实际参数:真实的/确定的/具体的 数据
repeated_attacks(3)
repeated_attacks(5)
repeated_attacks(10)

# 调试:
# F8:逐过程,不进入函数体内部
# F7:逐语句,进入函数体内部
