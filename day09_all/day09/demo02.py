"""
    作用域：变量起作用的范围。
        适用性:
            全局变量:在大范围(多个函数)内操作数据
            局部变量:在小范围(一个函数)内操作数据
"""
# -----------------全局变量:数据------------------
# 2. 全局变量:文件内部(函数外部)创建,适用于整个文件.
g01 = "a"
# -----------------函数:行为------------------
def func01():
    # 1. 局部变量: 函数内部创建的变量,只适用于函数内部.
    a = 10
    print(g01)  # 在局部作用域内,读取全局变量
# -----------------入口:调用------------------
func01()