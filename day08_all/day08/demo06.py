"""
    返回值 -- 语法
"""


# 价值1: return 返回数据
def func01():
    return 100


# 使用变量接收返回值
result = func01()


# 价值2: return 可以退出函数
def func02():
    print("func2执行喽")
    return 100  # 退出函数
    print("func2又执行喽")


result = func02()  # result 变量 接受到的是100
print(result)


# 特点:return 默认返回None
#     函数体如果没有return,相当于返回None
def func03():
    print("func3执行喽")
    # return  #  return None


result = func03()
print(result)
