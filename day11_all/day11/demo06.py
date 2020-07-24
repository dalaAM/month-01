"""
    # 1. 属性为什么操作私有变量?
    # @property
    # def data(self):
    #     return self.__data

    # @data.setter
    # def data(self, value):  # 3
    #     self.__data = value

    # 答: 要在保护圈内(公开的方法/属性)
"""


class MyClass:
    def __init__(self, data):
        self.data = data  # 2

    @property
    def data(self):
        # return self.a
        return self.__data  # 5

    @data.setter
    def data(self, value):
        print("保护逻辑")
        # self.a = value
        self.__data = value  # 3


c01 = MyClass(10)  # 1
# print(c01.data)# 4
# print(c01.a) # 如果不是私有变量,那么可以直接访问.就失去了保护价值.
