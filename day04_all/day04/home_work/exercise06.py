"""
    while 循环累加练习
    使用while循环累加下列数字：0  1  2  3
    使用while循环累加下列数字：2  3  4  5  6
    使用while循环累加下列数字：1  3  5  7
    使用while循环累加下列数字：8  7  6  5  4
    使用while循环累加下列数字：-1  -2  -3  -4  -5
"""
# 循环以前..创建变量
sum_value = 0
count = 0
while count <= 3:
    # 循环以内..累计运算
    sum_value += count
    count += 1
# 循环以外..获取结果
print(sum_value)

sum_value = 0
count = 2
while count <= 6:
    sum_value += count
    count += 1
print(sum_value)

sum_value = 0
count = 1
while count <= 7:
    sum_value += count
    count += 2
print(sum_value)

# 累计乘法
sum_value = 1  # 从1开始
count = 8
while count >= 4:
    sum_value *= count
    count -= 1
print(sum_value)

sum_value = 0
count = -1
while count >= -5:
    sum_value += count
    count -= 1
print(sum_value)
