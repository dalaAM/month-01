"""
    2. 为什么属性名称与实例变量名称相同?
         def __init__(self, data):
            self.data = data  # 4

        @property # data =  property(读取函数名称)
        def data(self):# 1 读取函数
            return self.__data # 7

        答: 使用属性 拦截 实例变量

    3. @data.setter 的含义?
        property 属性对象 由两个重要成员组成(读取函数,写入函数).
            @property 在创建属性对象并且添加读取函数
            @属性名.setter  在为属性对象添加写入函数
"""


class MyClass:
    def __init__(self, data):
        self.data = data  # 4

    @property # data =  property(读取函数名称)
    def data(self):# 1 读取函数
        return self.__data # 7

    @data.setter # data.setter(写入函数)
    def data(self, value): # 2 写入函数
        self.__data = value # 5


c01 = MyClass(10) # 3
print(c01.data)# 6
