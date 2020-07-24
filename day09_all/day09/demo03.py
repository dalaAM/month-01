"""
    global
"""
g01 = "a"


def func01():
    # g01 = "b" # 创建局部变量,没有修改全局变量
    # 局部作用域 修改 全局变量
    global g01 # 必须先声明全局变量
    g01 = "b"

func01()

print(g01) # ?