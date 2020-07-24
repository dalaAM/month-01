# 商品列表
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]


# 1. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_info(cid, commodity):
    print("商品编号%d,商品名称%s,商品单价%d." % (cid, commodity["name"], commodity["price"]))


def print_commodity_infos():
    for key, value in dict_commodity_infos.items():
        print_commodity_info(key, value)


# 2. 定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for key, value in dict_commodity_infos.items():
        if value["price"] < 20000:
            print_commodity_info(key, value)



# 定义函数,计算订单总价格：累加 (商品单价 * 数量)
def calculate_total_price_of_order():
    total_price = 0
    for order in list_orders:
        cid = order["cid"]
        commodity_info = dict_commodity_infos[cid]
        total_price += commodity_info["price"] * order["count"]
        # commodity_info = dict_commodity_infos[order["count"]]
        # total_price += commodity_info["price"] * order["count"]
    return total_price


# 3. 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.

# 4. 定义函数,计算订单总价格：累加 (商品单价 * 数量)

# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def order_max_by_count():
    min_order = list_orders[0]
    for r in range(1, len(list_orders)):
        if min_order["count"] < list_orders[r]["count"]:
            min_order = list_orders[r]
    print(min_order)


# 6. 根据购买数量对订单列表降序排列
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        for c in range(r + 1, len(list_orders)):
            if list_orders[r]["count"] < list_orders[c]["count"]:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
