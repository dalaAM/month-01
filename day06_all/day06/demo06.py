"""
    元组tuple
    exercise:exercise06,07
"""
# 1. 创建
# -- 写法1 元组名称 = (元素1,元素2)
tuple01 = (10, 20, 30, 40, 50)
list01 = ["悟空", "八戒"]
# 预留空间 --> 按需分配
# -- 写法2 元组名称 = tuple(其他容器)
tuple02 = tuple(list01)

# 2. 定位
# -- 索引
print(tuple01[1])  # 打印元组的第二个元素
# -- 切片
print(tuple01[:3])  # 打印元组的第三个元素 (10, 20, 30)

# 3. 如果元组只有一个元素,必须写逗号
# tuple03 = ("汉堡")
tuple03 = ("汉堡",)
print(type(tuple03))

# 4. 创建元组的小括号,可以省略
tuple04 = "汉堡", "薯条", "鸡翅"
print(tuple04)

# 5. 拆包
# a, b, c = ("汉堡", "薯条", "鸡翅")
# a, b, c = ["汉堡", "薯条", "鸡翅"]
a, b, c = "大薯条"
print(a)
print(b)
print(c)
