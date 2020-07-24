"""
    创建敌人类
    创建实例变量并保证数据在有效范围内
        姓名、血量、攻击力、防御力
              0-100  1 – 30、 0 – 20
"""

# 实例变量
class Enemy:
    def __init__(self, name, health, attack, defense):
        # 实例变量
        self.name = name
        # 属性
        self.health = health
        self.attack = attack
        self.defence = defense

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if 0 <= value <= 100:
            self.__health = value
        else:
            raise Exception("血量超过范围")  # 产生错误

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 1 <= value <= 30:
            self.__attack = value
        else:
            raise Exception("攻击不在范围内")

    # 快捷键:props + 回车
    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        if 0 <= value <= 30:
            self.__defence = value
        else:
            raise Exception("防御力超过范围")


mb = Enemy("灭霸", 100, 30, 20)
print(mb.__dict__)
print(mb.name)
print(mb.health)
print(mb.attack)
print(mb.defence)
