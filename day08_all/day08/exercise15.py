# 定义函数,在序列中获取最小值(不要使用内置函数)
# tuple01 = (43, 54, 5, 6, 76, 8, 9)
#
# min_value = tuple01[0]
# # 与后面进行比较
# for i in range(1, len(tuple01)):
#     if min_value > tuple01[i]:
#         min_value = tuple01[i]
# print(min_value)

def get_min_value(sequence):
    min_value = sequence[0]
    for i in range(1, len(sequence)):
        if min_value > sequence[i]:
            min_value = sequence[i]
    return min_value


tuple01 = (43, 54, 5, 6, 76, 8, 9)
print(get_min_value(tuple01))
