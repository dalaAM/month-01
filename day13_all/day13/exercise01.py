"""
    重写下列类型的str方法,体会重写
"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid}，部门编号是{self.did}，月薪是{self.money}"


class Department:
    def __init__(self, did, title):
        self.did = did
        self.title = title

    def __str__(self):
        return f"{self.title}的编号是{self.did}，"


class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration

    def __str__(self):
        return f"{self.name}的攻击率{self.atk_rate}需要sp{self.cost_sp}，持续时间{self.duration}"


e01 = Employee(1001, 9002, "师父", 60000)
print(e01) # e01.__str__()

d01 = Department(9001, "教学部")
print(d01)

s01 = Skill("乾坤大挪移", 1, -10)
print(s01)
