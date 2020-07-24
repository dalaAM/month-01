"""
    手雷爆炸,伤害了玩家(碎屏)和敌人(掉装备)
        要求:当增加其他事物,不影响手雷的代码.
            可能:鸭子(上天)....
    体会:
        开闭原则:增加鸭子,手雷代码不变
        依赖倒置:手雷使用攻击目标,手雷没有使用玩家.敌人
        继承价值:攻击目标抽象玩家敌人,统一概念(约束玩家和敌人受伤的做法一致),
                隔离手雷和具体攻击目标的变化
"""


class Grenade:
    def explode(self, target):
        print("手雷爆炸了！")
        # 先用:先行确定使用方法
        # 　调用攻击目标
        target.damage()


class AttackTarget:
    # 统一所有子类的行为
    def damage(self):
        pass


# 后做:后续完成工作的做法
# 继承攻击目标,重写受伤方法
class Player(AttackTarget):

    def damage(self):
        print("碎屏")


class Enemy(AttackTarget):

    def damage(self):
        print("掉装备")


# ----------------
grenade = Grenade()
grenade.explode(Player())
grenade.explode(Enemy())
