"""
    切片
        作用:
            定位多个元素
        语法:
            容器名称[开始:结束:间隔]
            for item in range(开始,结束,间隔):
                ...
    exercise:exercise02
"""
message = "我是齐天大圣"
print(len(message))
# 不包含结束
print(message[0:5:1])  # 我是齐天大
# 间隔默认1
print(message[0:5])  # 我是齐天大
# 开始默认为"开头"
print(message[:5])  # 我是齐天大
# 结束默认为"尾巴"
print(message[:])  # 我是齐天大圣
# 反转
# 开始是"尾巴"  结束是"开头"
print(message[::-1])  # 圣大天齐是我
# 是齐天大
print(message[1:-1])
# 大天齐是
print(message[-2:0:-1])

# 注意:
# 切片越界不报错
print(message[:99999])  # 应该写　print(message[:5])
print(message[:-99999:-1])  # 应该写　print(message[::-1]) 圣大天齐是我
print(message[1:1])  # 空
print(message[1:4:-1]) # 空
# print(message[1:4]) # 从索引为1到索引为3元素
