"""
    根据年月日,计算是这一年的第几天.
    公式：前几个月天数 + 当月天数
    例如：2020年5月10日
    计算：31  29  31  30 + 10
"""

year = int(input("请输入年份："))
month = int(input("请输入月份："))  # 5
day = int(input("请输入天："))
day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
days = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# total_day = 0
# for i in range(month - 1):  # 5 - 1  -->   0 1 2 3
#     total_day += days[i]
total_day = sum(days[:month - 1])
total_day += day
print(f"{year}年{month}月{day}日为这一年的第{total_day}天")
