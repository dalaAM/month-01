"""
    总结 Python 函数(方法)
"""


# ------------面向过程-------------
def func01():
    print("func01执行喽")

# 通过函数名称调用
func01()
# ------------面向对象-------------
class MyCalss:
    # 实例方法
    def func02(self):
        print("func02执行喽")
    # 类方法
    @classmethod
    def func03(cls):
        print("func03执行喽")

# 通过类名调用
MyCalss.func03()
# 通过对象调用
c01 = MyCalss()
c01.func02()

# MyCalss().func02()