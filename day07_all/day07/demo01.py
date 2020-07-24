"""

        列表推导式 [对变量的处理 for 变量 in 其他容器 if 条件]
        字典推导式 {对变量的处理 : 对变量的处理 for 变量 in 其他容器 if 条件}
"""
# 需求: key:0~9   value: key的平方
# dict01 = {}
# for number in range(10):
#     dict01[number] = number ** 2

dict01 = {number: number ** 2 for number in range(10)}
print(dict01)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 需求: key:0~9  能被3整除的  value: key的平方
# dict01 = {}
# for number in range(10):
#     if number % 3 == 0:
#         dict01[number] = number ** 2

dict01 = {number: number ** 2 for number in range(10) if number % 3 == 0}
print(dict01)  # {0: 0, 3: 9, 6: 36, 9: 81}
