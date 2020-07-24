from bll import CommodityController
from model import CommodityModel


class CommodityView:
    """
        商品视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 添加商品信息")
        print("2) 显示所有商品信息")
        print("3) 删除商品信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        # commodity.price = int(input("请输入商品单价:"))
        commodity.price = self.get_int("请输入商品单价:")
        self.__controller.add_commodity(commodity)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for commodity in self.__controller.list_commoditys:
            print(f"{commodity.name}的编号是{commodity.cid},单价是{commodity.price}")

    def __delete_commodity(self):
        # cid = int(input("请输入商品编号:"))
        cid = self.get_int("请输入商品编号:")
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def get_int(self, message):
        while True:
            try:
                data = int(input(message))
                return data
            except:
                print("重新输入")
