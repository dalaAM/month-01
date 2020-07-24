"""
    重写下列类型的__repr__方法,体会自定义对象拷贝
"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __repr__(self):
        return 'Employee(%d, %d, "%s", %d)' % (self.eid, self.did, self.name, self.money)


class Department:
    def __init__(self, did, title):
        self.did = did
        self.title = title

    def __repr__(self):
        return f'Department({self.did}, "{self.title}")'


class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration

    def __repr__(self) -> str:
        return f'Skill("{self.name}", {self.atk_rate}, {self.cost_sp},{self.duration})'


e01 = Employee(1001, 9002, "师父", 60000)
# 拷贝e01
str_code = e01.__repr__()  # <__main__.Employee object at 0x7f13fabef6a0>
e02 = eval(str_code)
print(e02.name)

d01 = Department(9001, "教学部")
# 拷贝d01
d02 = eval(d01.__repr__())
print(d02.title)

s01 = Skill("乾坤大挪移", 1, -10)
# 拷贝s01
s02 = eval(s01.__repr__())
print(s02.name)
