"""
4. 需求:
        在商品列表中,判断是否存在单价为12000的商品信息  False
        在商品列表中,判断是否存在编号1005的商品信息    True
5. 需求:
        在商品列表中,累加所有商品的单价
        在商品列表中,累加所有商品的商品编号
6. 需求:
        在商品列表中,删除编号是奇数的商品
        在商品列表中,删除单价小于500的商品
7. 需求:
        在商品列表中,根据单价对商品列表降序排列
        在商品列表中,根据商品名称字符长度降序排列
8. (选做)需求:
        在商品列表中,删除名称相同的商品
        在商品列表中,删除单价相同的商品

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

# 在商品列表中,判断是否存在单价为12000的商品信息  False
# 在商品列表中,判断是否存在编号1005的商品信息    True
result = IterableHelper.is_exists(list_commodity_infos, lambda item: item.price == 1200)
print(result)

result = IterableHelper.is_exists(list_commodity_infos, lambda item: item.cid == 1005)
print(result)

# 在商品列表中,累加所有商品的单价
# 在商品列表中,累加所有商品的商品编号
result = IterableHelper.sum(list_commodity_infos, lambda item: item.price)
print(result)
result = IterableHelper.sum(list_commodity_infos, lambda item: item.cid)
print(result)

# 在商品列表中,删除编号是奇数的商品
# 在商品列表中,删除单价小于500的商品
# IterableHelper.delete_all(list_commodity_infos, lambda item: item.cid % 2)

# IterableHelper.delete_all(list_commodity_infos, lambda item: item.price < 500)
# for item in list_commodity_infos:
#     print(item.__dict__)

"""
#  在商品列表中,删除名称相同的商品
def delete_duplicates():
    # 取数据
    for r in range(len(list_commodity_infos)-1,0,-1):
        # 作比较
        for c in range(r):
            # 有相同
            if list_commodity_infos[r].name ==  list_commodity_infos[c].name:
                # 删后面
                del list_commodity_infos[r]
                # 停止比较
                break

delete_duplicates()
for item in list_commodity_infos:
    print(item.__dict__)

#  在商品列表中,删除单价相同的商品

def delete_duplicates():
    for r in range(len(list_commodity_infos)-1,0,-1):
        for c in range(r):
            if list_commodity_infos[r].price ==  list_commodity_infos[c].price:
                del list_commodity_infos[r]
                break

def delete_duplicates(func):
    # 取数据
    for r in range(len(list_commodity_infos)-1,0,-1):
        # 作比较
        for c in range(r):
            # 有相同
            # if list_commodity_infos[r].name ==  list_commodity_infos[c].name:
            if func(list_commodity_infos[r]) ==  func(list_commodity_infos[c]):
                # 删后面
                del list_commodity_infos[r]
                # 停止比较
                break

delete_duplicates(lambda item:item.name)
delete_duplicates(lambda item:item.price)
"""


IterableHelper.delete_duplicates(list_commodity_infos,lambda item:item.name)
for item in list_commodity_infos:
    print(item.__dict__)





