"""
    创建狗类
        数据：品种、爱称、年龄、体重
        行为：吃、叫
    实例化两个对象并调用其方法
    画出内存图
"""

# 类名：所有单词首字母大写，多个单词不要使用下划线隔开．
class Dog:
    def __init__(self, bread, name, age, weight):
        self.bread = bread
        self.nick_name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print("%s吃饭啦." % self.nick_name)

    def bark(self):
        print("%s汪汪叫." % self.nick_name)

d01 = Dog("金毛", "旺财", 2, 70)
d01.eat()
d01.bark()

d02 = Dog("拉布拉多", "米咻", 4, 60)
d02.eat()
d02.bark()
