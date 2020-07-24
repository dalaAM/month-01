"""
    隐藏成员: 向类外隐藏成员
        命名:双下划线开头
        本质:单下划线+类名+实例变量名
            例如: _MyClass__data
"""


# class MyClass:
#     def __init__(self):
#         self.data = 10
#
#     def func01(self):
#         print("func01执行喽")
#
#
# c01 = MyClass()
# print(c01.data)
# c01.func01()

# 障眼法:孙悟空变成了房子
class MyClass:
    def __init__(self):
        self.__data = 10

    def __func01(self):
        print("func01执行喽")

    def func02(self):
        # 类中可以访问私有变量
        print(self.__data)


c01 = MyClass()
# print(c01.__data) # 君子:类外不能访问私有变量
# print(c01._MyClass__data)  # "臭流氓":使用单下划线+类名+实例变量名访问

# c01.__func01()
# dir() 可以获取对象所有成员
print(dir(c01))  # _MyClass__func01

c01.func02()

# class MyClass2:
#     pass
#
# c02 = MyClass2()
# c02.__data = 10 # 不是私有变量
# print(c02.__data) # 可以访问
