"""
    排序算法
        [取]出前几个数据(不要最后一个)
            与后面元素进行[比]较
"""
list01 = [4, 54, 5, 6, 67, 788]
# list01[0]
# for i in range(1, len(list01)):
#     if list01[0] < list01[i]:
#         list01[0], list01[i] = list01[i], list01[0]

# list01[1]
# for i in range(2, len(list01)):
#     if list01[1] < list01[i]:
#         list01[1], list01[i] = list01[i], list01[1]
# print(list01)

# 获取数据
for r in range(len(list01) - 1):
    # 与后面元素比较
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
