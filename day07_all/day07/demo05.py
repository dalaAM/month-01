"""
    变量交换算法:
        a,b = b,a
    获取极值算法:
        假设第一个就是最大
        使用假设的与后面的进行比较,如果发现更大,则替换.
"""
# 获取最大值
list01 = [43, 45, 8, 6, 4, 8, 55, 33]
max_value = list01[0]
for i in range(1, len(list01)):
    if max_value < list01[i]:
        max_value = list01[i]
print(max_value)
