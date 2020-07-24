"""
    玩家攻击敌人(掉装备)
    敌人攻击玩家(碎屏)
    要求:玩家和敌人还可能被其他目标攻击,也可能攻击其他目标.
"""

"""
class AttackTarget:
    def damage(self):
        pass


class Player(AttackTarget):
    def attack(self, target):
        print("打你")
        target.damage()

    def damage(self):
        print("碎屏")


class Enemy(AttackTarget):
    def attack(self, target):
        print("打你")
        target.damage()

    def damage(self):
        print("掉装备")
 
p01  = Player()
e01 = Enemy()
p01.attack(e01)
e01.attack(p01)
"""


class Character:
    # 所有角色攻击方式相同
    def attack(self, target):
        print("打你")
        target.damage()

    # 所有角色受伤逻辑不同
    def damage(self):
        pass

class Player(Character):
    def damage(self):
        print("碎屏")

class Enemy(Character):
    def damage(self):
        print("掉装备")


p01 = Player()
e01 = Enemy()
p01.attack(e01)
e01.attack(p01)
