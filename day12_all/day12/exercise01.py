"""
    小明请保洁打扫卫生
        客户 -- 通知/预约
        保洁员 -- 打扫
"""


# 1.  小明每次通知新保洁
# class Client:
#     def __init__(self, name=""):
#         self.name = name
#
#     def notify(self):
#         print(self.name,"通知")
#         cleaner = Cleaner()
#         cleaner.cleaning()
#
# class Cleaner:
#     def cleaning(self):
#         print("打扫卫生")
#
# xm = Client("小明")
# xm.notify()

# 2.  小明通知自己的保洁员
# class Client:
#     def __init__(self, name=""):
#         self.name = name
#         self.cleaner = Cleaner()
#
#     def notify(self):
#         print(self.name,"通知")
#         self.cleaner.cleaning()
#
# class Cleaner:
#     def cleaning(self):
#         print("打扫卫生")
#
# xm = Client("小明")
# xm.notify()


# 3. 小明通知家政服务(参数)
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, household_service):
        print(self.name, "通知")
        household_service.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)
