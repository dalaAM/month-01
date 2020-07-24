"""
    list --> str
    将多个字符串拼接为一个。
    result = "连接符".join(列表)
    exercise:exercise02

"""
# 语法
list01 = ["a", "b", "c"]
result = "-".join(["a", "b", "c"])
print(result)

# 应用:根据条件拼接一个字符串
# range(10)  -->   "0123456789"
# 缺点: 每次拼接+都会产生新字符串对象,旧的成为垃圾(1,12,123,1234...)
# 解决: 频繁修改不可变对象时,使用可变对象代替.
# result = ""
# for item in range(10):
#     result = result + str(item)
# print(result)

# 每次append,都追加到原有列表
result = []
for item in range(10):
    result.append(str(item))
result = "".join(result)
print(result)
