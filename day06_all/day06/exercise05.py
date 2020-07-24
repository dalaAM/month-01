"""
    画图
"""
name = "张无忌"
names = ["赵敏", "周芷若"]
tuple01 = ("张翠山", name, names)
name = "无忌哥哥"
# 木有修改元组,而是列表
tuple01[2][0] = "敏儿"
print(tuple01)  # ?
