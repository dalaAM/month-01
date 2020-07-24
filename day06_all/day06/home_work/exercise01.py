"""
    1. 根据列表中的数字,重复生成*.
        list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    效果：
        *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *

    2. 将列表中的数字累乘
        list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    结果：806400

    3. 将列表中整数的个位不是5和3的数字存入另外一个列表
        list03 = [25, 63, 27, 75, 70, 83, 27]
    结果:[27, 70, 27]
"""
list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
for item in list01:
    print("*" * item)

list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
result = 1  # 因为1乘以任何数字,都不改变.
for item in list02:
    result *= item
print(result)

list03 = [25, 63, 27, 75, 70, 83, 27]
result = []
for item in list03:
    unit = item % 10
    if unit == 5 or unit == 3:
        continue
    result.append(item)
print(result)
