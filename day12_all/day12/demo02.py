"""
    封装设计思想
        理念:分而治之  变则疏之
        步骤:识别(行为)变化  分配职责   建立交互
    需求:老张开车去东北
        变化:老张/老李/老王/老赵...   数据不同,类不做区分.
            人 -- 去
            车 -- 行驶
"""

# 建立交互(跨类调用)
# 1. 以需求为导向 -- 业务情景(人开车....)
# 2. 确定被调用的成员(实例/类)
# 3. 根据需求选择不同写法
#   (1) 直接创建对象调用.
#   (2) 在构造函数中创建对象.

#   (3) 将对象通过参数传递进来.

"""
#   (1) 直接创建对象调用.
#      语义:老张出去一趟使用一辆新车
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, pos):
        print(self.name, "去", pos)
        c01 = Car()
        c01.run()

class Car:

    def run(self):
        print("汽车在行驶")


# 数据不同 使用 对象区分
lz = Person("老张")
ll = Person("老李")
lw = Person("老王")

lz.go_to("东北")
lz.go_to("家")
"""

"""
#   (2) 在构造函数中创建对象.
#      语义:老张开自己的车出去
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self, pos):
        print(self.name, "去", pos)
        self.car.run()
        
class Car:
    def run(self):
        print("汽车在行驶")
# 数据不同 使用 对象区分
lz = Person("老张")
lz.go_to("东北")
lz.go_to("家")
"""


#   (3) 将对象通过参数传递进来.
#      语义:老张通过参数(变量)出去,没有和车绑定关系
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle, pos):
        print(self.name, "去", pos)
        vehicle.run()

class Car:
    def run(self):
        print("汽车在行驶")

# 测试
# 数据不同 使用 对象区分
lz = Person("老张")
c01 = Car()
lz.go_to(c01, "东北")
# 换其他交通工具
lz.go_to(c01, "回家")
