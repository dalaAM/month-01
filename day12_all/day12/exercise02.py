"""
    玩家攻击(攻击力)敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
    敌人攻击(攻击力)玩家，玩家受伤(减血,碎屏)后可能si亡(游戏结束)
"""


# 需求1:  玩家攻击打敌人
# 1. 单向攻击 -- 基础版本
# class Player:
#     def attack(self, target):
#         print("玩家攻击")
#         target.damage()
#
# class Enemy:
#     def damage(self):
#         print("(⊙o⊙)… 敌人受伤啦")
#
# p01 = Player()
# e01 = Enemy()
# p01.attack(e01)
# p01.attack(e01)

# 需求2: 玩家攻击(攻击力)敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
# 2. 单向攻击
# class Player:
#     def __init__(self, atk=50):
#         self.atk = atk
#
#     def attack(self, target):
#         print("玩家攻击")
#         target.damage(self.atk)
#
# class Enemy:
#     def __init__(self, hp=100):
#         self.hp = hp
#
#     def damage(self, value):
#         print("(⊙o⊙)… 敌人受伤啦")
#         self.hp -= value
#         if self.hp <= 0:
#             print("播放死亡动画")


# p01 = Player()
# e01 = Enemy()
# p01.attack(e01)
# p01.attack(e01)

# 需求3:  玩家攻击(攻击力)敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
#        敌人打玩家
# 3. 双向攻击 基础版本
# class Player:
#     def __init__(self, atk=50):
#         self.atk = atk
#
#     def attack(self, target):
#         print("玩家攻击")
#         target.damage(self.atk)
#
#     def damage(self):
#         print("(⊙o⊙)… 玩家受伤啦")
#         print("碎屏")
#
#
# class Enemy:
#     def __init__(self, hp=100):
#         self.hp = hp
#
#     def damage(self, value):
#         print("(⊙o⊙)… 敌人受伤啦")
#         self.hp -= value
#         if self.hp <= 0:
#             print("播放死亡动画")
#
#     def attack(self,target):
#         print("敌人攻击")
#         target.damage()
#
#
# p01 = Player()
# e01 = Enemy()
# p01.attack(e01)
# e01.attack(p01)

# 需求4: 玩家攻击(攻击力)敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
#       敌人攻击(攻击力)玩家，玩家受伤(减血,碎屏)后可能si亡(游戏结束)

# 4. 双向攻击本
class Player:
    def __init__(self, hp=200, atk=50):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print("玩家攻击")
        target.damage(self.atk)

    def damage(self, value):
        print("(⊙o⊙)… 玩家受伤啦")
        print("碎屏")
        self.hp -= value
        if self.hp <= 0:
            print("游戏结束")

class Enemy:
    def __init__(self, hp=100, atk=10):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("(⊙o⊙)… 敌人受伤啦")
        self.hp -= value
        if self.hp <= 0:
            print("播放死亡动画")

    def attack(self, target):
        print("敌人攻击")
        target.damage(self.atk)


p01 = Player()
e01 = Enemy()
p01.attack(e01)
e01.attack(p01)
