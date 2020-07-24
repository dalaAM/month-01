"""
    根据下列代码,定义函数,对列表进行升序排列
"""


# list01 = [4, 54, 5, 6, 67, 788]
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] > list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01)

def ascending_sort(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                # 2. 修改可变对象
                list_target[r], list_target[c] = list_target[c], list_target[r]


# 1. 传入可变对象(列表)
list01 = [4, 54, 5, 6, 67, 788]
ascending_sort(list01)
# 3. 函数执行后,数据受到影响
print(list01)  # 注意:排序的结果不是函数返回值
