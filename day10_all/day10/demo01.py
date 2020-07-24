"""
    str 是 类    "悟空"是 对象
    int 是 类     100 是  对象

    现实事物  -抽象->  类  -具体-> 对象
"""
# 全局变量只有一份
name = "双儿"
face_score = 92
money = 5000
# 实例变量每个对象都有一份(互补影响)

class Wife:
    """
        老婆 抽象/概念/模板
    """

    # 数据
    def __init__(self, name, money, face_score=60):
        self.name = name
        self.face_score = face_score
        self.money = money

    # 行为
    def work(self):
        print(self.name + "工作挣钱")


# 创建(实例化)对象
w01 = Wife("双儿", 50000, 92)  # 调用 构造函数__init__
# 通过对象调用方法
w01.work()  # 会自动传递对象地址 work(w01)


w02 = Wife("建宁", 9000000, 89)
w02.work()#work(w02)
