"""
    创建子类：狗(跑)，鸟类(飞)
    创建父类：动物(吃)
    体会子类复用父类方法
        体会: 是一种
                 对象   类型
                 类型   类型
             是
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")
        self.eat()


class Bird(Animal):
    def fly(self):
        print("飞")
        super().eat()


d01 = Dog()
d01.run()
d01.eat()
