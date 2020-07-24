"""
    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""


class Car:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand="", speed=0, battery_capacity=0, charging_power=0):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


e01 = Electrocar("本田", 300, 15000, 1000)
print(e01.__dict__)
