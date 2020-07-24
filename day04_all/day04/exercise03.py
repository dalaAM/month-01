"""
    累加0 1 2 3 4 5 6 7 8
    累加3 4 5 6 7 8 9 10
    累加2 4 6 8 10 12
    累加8 7 6 5 4 3
    累加-1 -2 -3 -4 -5 -6
"""
# 循环前 ... 创建
count = 0
for item in range(9):
    count += item  # 循环中 ... 累加
print(count)  # 循环后 ... 结果

count = 0
for item in range(3, 11):
    count += item
print(count)

count = 0
for item in range(2, 13, 2):
    count += item
print(count)

count = 0
for item in range(8, 2, -1):
    count += item
print(count)

count = 0
for item in range(-1, -7, -1):
    count += item
print(count)
