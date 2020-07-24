"""
    统计Wife类创建了多少对象(类变量记录创建的对象数量)
    画出内存图
        w01 = Wife("建宁")
        w02 = Wife("双儿")
        w03 = Wife("苏荃")
        Wife.print_count()
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("老爷,您娶了%d个老婆了." % cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("建宁")
w02 = Wife("双儿")
w03 = Wife("苏荃")
Wife.print_count()
