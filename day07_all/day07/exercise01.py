"""
    练习1：将两个列表，合并为一个字典
            姓名列表["张无忌","赵敏","周芷若"]
            房间列表[101,102,103]
    练习2：颠倒练习1字典键值
"""
names = ["张无忌", "赵敏", "周芷若"]
rooms = [101, 102, 103]
dict01 = {names[i]: rooms[i] for i in range(len(names))}

dict02 = {value: key for key, value in dict01.items()}
print(dict02)

# 需求: 根据值查找键
# 解决方案1: 键值对颠倒
# 解决方案2:
for key, value in dict01.items():
    if value == 103:
        print(key)
