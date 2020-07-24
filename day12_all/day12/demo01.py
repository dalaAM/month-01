"""
    属性各种写法
"""
# 一.读写属性
#   1. 快捷键:props + 回车
#   2. 属性名与实例变量名相同
#   3. 在读写方法中操作私有变量
class MyClass01:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


c01 = MyClass01()
print(c01.data)


# 二.只读取属性
#   1. 在构造函数中创建私有变量
#   2. 快捷键:prop + 回车
class MyClass02:
    def __init__(self):
        self.__data = 100

    @property
    def data(self):
        return self.__data


c02 = MyClass02()
print(c02.data)


# c02.data = 10 # AttributeError: can't set attribute


# 三.只写属性
#   1.创建属性对象
#   2.为属性对象添加写入函数
class MyClass03:
    def __init__(self, data=0):
        self.data = data

    # 创建属性对象
    data = property()

    @data.setter
    def data(self, value):
        self.__data = value


c03 = MyClass03(10)
c03.data = 20
print(c03.__dict__)
# print(c03.data)# AttributeError: unreadable attribute
