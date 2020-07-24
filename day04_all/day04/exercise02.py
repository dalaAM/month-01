"""
    在终端中录入一个整数, 打印每位相加和。
"""
number = input("请输入一个数：")  # "1234"

sum = 0
for item in number:  # "1"               2
    sum += int(item)  # "1" -> 1       1 + 2
print("结果是:" + str(sum))
