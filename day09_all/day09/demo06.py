"""
    函数参数
        实际参数:与 形参 对应
            1.位置实参:按顺序
                2.序列实参:拆
            3.关键字实参:按名称
                4.字典实参:拆
        形式参数：约束实参传递方式
            5.默认形参:实参可选
            6.位置形参:实参必填
            7.命名关键字形参:必须关键字实参
            不定长参数
                8.星号元组形参:位置实参数量无限　　　合
                9.双星号字典形参:关键字实参数量无限　合
"""


# 1. 默认形参注意:必须从右向左依次存在
def func01(p1, p2=0, p3=0):
    print(p1)
    print(p2)
    print(p3)

func01(1)

# 2.位置形参:必填
def func02(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 3.星号元组形参：将实参合并为一个元组（只适用于位置实参）
# 价值：位置实参数量可以无限
def func03(*args):
    print(args)


func03(1, 2, 3)  # 函数内部得到的是一个元组 (1,2,3)
func03()  # 函数内部得到的是一个空元组 ()


# func03(a=1,b=2)#TypeError: func03() got an unexpected keyword argument 'a'

# 4. 命名关键字形参:强调必须是关键字实参
#  -- 星号元组形参后面的参数 a, b, c
def func04(*args, a, b, c):
    print(args)
    print(a)
    print(b)
    print(c)


func04(1, 2, 3, 4, a=5, b=6, c=7)


#  -- 星号后面的参数 a, b, c
# 第一个参数是必填(重要),后面两个参数是可选(不重要)
def func05(a, *, b=0, c=0):
    print(a)
    print(b)
    print(c)


func05(5)
# func05(5,6,7)　　
func05(5, b=6)
func05(5, c=7)
func05(5, b=6, c=7)


# 5.　双星号字典形参
def func06(**kwargs):
    print(kwargs)


func06()  # 函数内部得到的是空字典
func06(a=1, b=2)  # 函数内部得到的是{"a":1,"b":2}
# func06(1,2,3,4)# TypeError: func06() takes 0 positional arguments but 4 were given
