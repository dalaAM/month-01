"""
    业务逻辑层
""" 
from dal import HouseDao
class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self):
        return self.__list_houses

    def get_house_by_max_price(self):
        return max(self.__list_houses,key = lambda house:house.total_price)

    def get_house_by_min_area(self):
        return min(self.__list_houses,key = lambda house:house.area)
