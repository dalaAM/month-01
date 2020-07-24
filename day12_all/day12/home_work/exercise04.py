"""
    1. 定义函数,将列表中奇数设置为1
    2. 定义函数,将列表中奇数删除
    测试数据:[3,4,5,6,7,8,9]

    结论:在列表中删除多个元素,倒序删除
"""


def change_odd_to_one(list_target):
    for i in range(len(list_target)):
        if list_target[i] % 2:
            list_target[i] = 1


list01 = [3, 4, 5, 6, 7, 8, 9]
change_odd_to_one(list01)
print(list01)


# def delete_all_by_odd(list_target):
# 问题1:越界
# 删之前数据有7个,随着删除数据减少,
# 但是循环变量i依然执行到7停止,造成索引越界的错误.
# 问题2:漏删
# 删除前面元素,后面元素会自动向前移动(索引减小)
# for i in range(len(list_target)):
#     if list_target[i] % 2:
#         del list_target[i]

def delete_all_by_odd(list_target):
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] % 2:
            del list_target[i]
            # 因为remove内部也是循环判断,所以不建议,
            # list_target.remove(list_target[i])


list01 = [3, 4, 5, 6, 7, 8, 9]
delete_all_by_odd(list01)
print(list01)
