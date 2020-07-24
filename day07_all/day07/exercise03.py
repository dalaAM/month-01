# 二维列表名[行索引][列索引]
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

# 打印出3/9/12
print(list01[0][2])
print(list01[1][3])
print(list01[2][1])

# (每行一个)循环打印6, 7, 8, 9, 10
for item in list01[1]:
    print(item)
# (每行一个)循环打印15,14,13,12,11
for i in range(len(list01[2]) - 1, -1, -1):
    print(list01[2][i])
# (每行一个)循环打印1,6,11
# print(list01[0][0])
# print(list01[1][0])
# print(list01[2][0])
# for r in range(3):# 0 1 2
#     print(list01[r][0])
for r in range(len(list01)):  # 0 1 2
    print(list01[r][0])

# (每行一个)循环打印14,9,4
# print(list01[2][3])
# print(list01[1][3])
# print(list01[0][3])
# for r in range(2, -1, -1):
#     print(list01[r][3])
for r in range(len(list01) - 1, -1, -1):
    print(list01[r][3])
# 以表格状打印每个元素(不要逗号)
for line in list01:
    for item in line:
        print(item, end="\t")  # \t 水平制表格
    print()
