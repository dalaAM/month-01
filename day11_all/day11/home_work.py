# 画出下列代码内存图

class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color


# 1
list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]

# 2
for item in list_phones:
    if item.color == "白色":
        item.price = 0
print(list_phones[0].price)  # 5999
print(list_phones[-1].price)  # 0


# 3
def find():
    for item in list_phones:
        if item.brand == "华为2":
            return item


result = find()
# <__main__.Phone object at 0x7fa795409fd0>
# print(result) # 打印 自定义对象 的 格式:<__main__.类名 object at 内存地址>
# print(result.brand, result.price, result.color)  # ?
print(result.__dict__)# 对象所有实例变量{'brand': '华为2', 'price': 6999, 'color': '红色'}