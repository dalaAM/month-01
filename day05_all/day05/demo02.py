"""
    索引index
        作用:
            定位单个元素
        语法:
            容器名称[整数]
"""
message = "我是齐天大圣"
print(message[0])  # 获取第一个元素
# print(message[-6])  # 获取第一个元素

print(message[-1])  # 获取最后一个元素
# print(message[5])  # 获取最后一个元素

# 注意: 索引不能越界
# print(message[99999])# IndexError
# print(message[-99999])# IndexError
print(message[-0])  # 相当于print(message[0])
