"""
    玩家(攻击力)攻击敌人(血量)(掉装备),还可能死亡(播放死亡动画)
    敌人(攻击力)攻击玩家(血量)(碎屏),还可能死亡(游戏结束)
    要求:在day14/home_work/exercise03基础上增加数据,和血量为零死亡功能.
"""

class Character:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    # 所有子类完整共性(子类不用重写)
    def attack(self, target):
        print("打你")
        target.damage(self.atk)

    # 所有子类部分共性(子类重写需要通过super调用父)
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.death()

    # 所有子类行为共性(没有实现共性,子类重写)
    def death(self):
        pass


class Player(Character):
    def damage(self, value):
        print("碎屏")
        super().damage(value)

    def death(self):
        print("游戏结束")


class Enemy(Character):
    def damage(self, value):
        print("掉装备")
        super().damage(value)

    def death(self):
        print("播放死亡动画")


p01 = Player(100, 50)
e01 = Enemy(50, 30)
e01.attack(p01)
p01.attack(e01)
