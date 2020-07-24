"""
    使用封装数据的思想
        1. 创建商品类(商品编号,商品名称,商品单价)/订单类,
        2. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
        3. 定义函数,打印商品单价小于2万的商品信息

        4. 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
        5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
        6. 根据购买数量对订单列表降序排列

"""

# ----------------------数据模板-----------------------------
class Commodity:
    """
        商品类(模板)
    """

    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


class Order:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count

# ----------------------数据对象-----------------------------

# 商品列表
list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30)
]

list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2)
]

# ----------------------函数-----------------------------

def print_single_commodity(commodity):
    print(f"商品编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")


# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)


# 2.  定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)


# 3.  定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
def print_order_infos():
    for order in list_orders:
        for commodity in list_commodity_infos:
            print(f"商品名称{commodity.name},商品单价:{commodity.price},数量{order.count}.")
            break  # 跳出内层循环


# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def order_max_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value.count < list_orders[i].count:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_orders[i]
    return max_value


# 6. 根据购买数量对订单列表降序排列
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        for c in range(r + 1, len(list_orders)):
            if list_orders[r].count < list_orders[c].count:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]

# ----------------------测试入口-----------------------------

result = order_max_by_count()
print(result)  # <__main__.Order object at 0x7f84774a96a0>
print(result.__dict__)  # {'cid': 1002, 'count': 3}

descending_order_by_count()
# print(list_orders)# [<__main__.Order object at 0x7f0b85261668>, <__main__.Order object at 0x7f0b852616a0>, <__main__.Order object at 0x7f0b85261630>]
for item in list_orders:
    print(item.__dict__)

"""
# 面向过程代码
# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


# --------------------------操作--------------------------

def print_single_commodity(commodity):
    print(f"商品编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")


# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        # print(f"商品编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")
        print_single_commodity(commodity)


# 2.  定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity["price"] < 20000:
            # print(f"商品编号:{commodity['cid']}商品名称:{commodity['name']}商品单价:{commodity['price']}")
            print_single_commodity(commodity)


# 3.  定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
def print_order_infos():
    for order in list_orders:  # 遍历所有订单
        # order["cid"] --> 1001  -->
        for commodity in list_commodity_infos:  # 遍历所有商品信息
            # commodity["cid"] --> 1001
            # 使用订单中的商品编号 在 商品信息中查找(商品)
            # if order["cid"] in commodity.values():
            # if order["cid"] == commodity["cid"]:
            print(f"商品名称{commodity['name']},商品单价:{commodity['price']},数量{order['count']}.")
            break  # 跳出内层循环


# 4. 定义函数,计算订单总价格：累加 (商品单价 * 数量)
def calculate_total_price_of_order():
    total_price = 0
    for order in list_orders:  # 遍历每条订单
        # 数量 order["count"]
        # 商品编号 order["cid"]
        for commodity in list_commodity_infos:  # 查找价格
            if order["cid"] == commodity["cid"]:
                total_price += commodity["price"] * order["count"]
                break  # 如果查找到商品，那么停止查找。
    return total_price


# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def order_max_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value["count"] < list_orders[i]["count"]:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_orders[i]
    return max_value


# 6. 根据购买数量对订单列表降序排列
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        for c in range(r + 1, len(list_orders)):
            if list_orders[r]["count"] < list_orders[c]["count"]:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]


# --------------------------入口--------------------------
# 测试
# print_commodity_infos()
# print_price_in_2w()
# print_order_infos()
# total_price = calculate_total_price_of_order()
# print(total_price)
# print(order_max_by_count())
descending_order_by_count()
print(list_orders)
"""
