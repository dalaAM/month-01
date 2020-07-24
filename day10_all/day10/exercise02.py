class Phone:  # ----------------类
    def __init__(self, brand, price, color):
        self.brand = brand  # ------------self.实例变量
        self.price = price
        self.color = color

    def call(self):  # ------------ 实例方法
        print(self.brand + "通话")


iphone = Phone("苹果", 7800, "red")  # ---------对象
iphone.call()

# 画出下列代码内存图
# 1
i01 = iphone
iphone.price += 200
print(i01.price)  # 8000

# 2
huwei = Phone("华为", 5999, "blue")
huwei.call()


def func01(p1):
    p1.color = "蓝色"


func01(huwei)
print(huwei.color)  # "蓝色"
