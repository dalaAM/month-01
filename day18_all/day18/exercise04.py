"""
    需求:
        在商品列表中,查找所有商品名称
        在商品列表中，查找所有商品编号和单价
        .....
        查找满足条件的元素数量

    步骤:
        1. 实现完整功能
        2. 将不变的定义到IterableHelper类中
        3. 在当前模块中调用IterableHelper类中代码
               不变的 + 变化的(lambda)
"""
from common.iterable_tools import IterableHelper


class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]


def select01():
    for item in list_commodity_infos:
        yield item.name


for name in select01():
    print(name)


def select02():
    for item in list_commodity_infos:
        yield item.cid, item.price


for name in select02():
    print(name)
"""
# 提取不变的
def select(list_target,func):
    for item in list_target:
        # yield item.name
        yield func(item) # 调用lambda函数，传递列表的每个元素

for name in select(list_commodity_infos,lambda com:com.name):
    print(name)

for name in select(list_commodity_infos,lambda com:(com.cid,com.price)):
    print(name)
"""
for name in IterableHelper.select(list_commodity_infos, lambda com: com.name):
    print(name)
