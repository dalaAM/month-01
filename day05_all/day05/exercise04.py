"""
    list_city = ["黑龙江", "香港", "台湾"]
    list_cofirmed = [138, 104, 95]
    list_total = [944, 1040, 440]
    1. 打印以上列表的最后一个元素 / 前两个元素
    2. 将台湾疫情信息存入新列表中
    3. 修改以上列表的元素如下:
        ["黑龙江", "香港", "台湾"] --> ["hlj", "xg", "tw"]
        104 -> 105
        1040 -> 1041
"""
list_city = ["黑龙江", "香港", "台湾"]
list_cofirmed = [138, 104, 95]
list_total = [944, 1040, 440]
#  1. 打印以上列表的最后一个元素 / 前两个元素
print(list_city[-1])
print(list_cofirmed[-1])
print(list_total[-1])

print(list_city[:2])
print(list_cofirmed[:2])
print(list_total[:2])

# 2.将台湾疫情信息存入新列表中
list_taiwan = [list_city[-1], list_cofirmed[-1], list_total[-1]]

# 3. 修改以上列表的元素如下:
# list_city = ["hlj", "xg", "tw"]  # 修改变量list_city
list_city[:] = ["hlj", "xg", "tw"]  # 修改列表中的元素
print(list_city)

list_cofirmed[1] = 105  # 修改列表第二个元素105
list_total[1] += 1  # 列表第二个元素 自增1
