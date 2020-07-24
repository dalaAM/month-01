"""
    day07/home_work/exercise03
    根据下列代码,定义函数,获取一个范围内的所有闰年.
"""


# list_year = [item for item in range(1970, 2051)
#              if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]
# print(list_year)

# def calculate_leap_year_in_range(begin, end):
#     return [item for item in range(begin, end)
#             if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]

def is_leap_year(year):
    """
        判断闰年
    :param year:
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def calculate_leap_year_in_range(begin, end):
    """

    :param begin:
    :param end:
    :return:
    """
    return [year for year in range(begin, end) if is_leap_year(year)]

print(calculate_leap_year_in_range(1999, 2020))
