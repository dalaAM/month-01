"""
    exercise:根据各种条件,查询结果.
"""


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


# 练习1:定义函数,在商品列表中,获取编号大于1004的所有商品信息.
def commodity_cid_over_1004():
    """

    :return:
    """
    for com in list_commodity_infos:
        if com.cid > 1004:
            yield com


# 返回多个结果使用生成器.  --->  获取数据不灵活
# result = commodity_cid_over_1004()
# 解决方案:  容器(生成器对象)
# 惰性操作 --> 立即操作
result = tuple(commodity_cid_over_1004())
for item in result:
    print(item.__dict__)


# 练习2:定义函数,在商品列表中,获取价格小于10000的所有商品信息.
def get_commodity_price_less_10000():
    for commodity in list_commodity_infos:
        if commodity.price < 10000:
            yield commodity


for commodity in get_commodity_price_less_10000():
    print(commodity.__dict__)


# 练习3:定义函数,在商品列表中,获取编号是1006的商品信息.
def commodity_cid_is_1006():
    for com in list_commodity_infos:
        if com.cid == 1006:
            return com


commodity = commodity_cid_is_1006()
print(commodity.name)
