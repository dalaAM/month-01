"""
    函数参数
        实际参数
            位置实参
            关键字实参
        形式参数
            默认实参
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 1. 位置实参: 与形参一一对应
func01(1, 2, 3)
# func01(1,2,3,4) # TypeError: func01() takes 3 positional arguments but 4 were given
# func01(1, 2)# TypeError: func01() missing 1 required positional argument: 'p3'

# 2. 关键字实参: 与形参按名字对应
func01(p1=1, p2=2, p3=3)
func01(p2=2, p1=1, p3=3)  # 顺序无所谓


# func01(p2 = 2) # 报错,缺少p1/p3

# 3. 默认形参:实参可选
def func02(p1="", p2=0.0, p3=0):
    print(p1)
    print(p2)
    print(p3)

func02(p2=2)
func02()
func02(1, 2, 3)

