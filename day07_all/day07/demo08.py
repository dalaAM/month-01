"""
    容器总结
        字符串:存储字符编码值,不可变,序列
            价值:表达文字信息
        列表:存储变量,可变,序列
            价值:定位灵活(索引/切片)/存储单一维度信息
        元组:存储变量,不可变,序列
            价值:省内存
        字典:存储键值对,可变,散列
            价值:定位快/存储多维度信息 hlj = {"city": "黑龙江", "cofirmed": 138, "total": 944}
        集合:存储键,可变,散列
            价值:去重复/数学运算

        不可变:所有数据的本质(在内存中开辟空间后,空间不能改变大小),内存会按需分配
        可变:在不可变基础上,赋予了扩容机制,内存会预留空间

        序列:有顺序,省内存,定位灵活(可以使用索引切片)
        散列:无顺序,费内存,定位快
"""
# 基本操作
# (一)列表
# 1. 创建
list01 = []
list02 = ["纪小强", "于全胜", "王琳雅"]

# 2. 列表 --> 字典
dict02 = {item: len(item) for item in list02}
list03 = [('name', '纪小强'), ('age', 26), ('score', 98)]
dict03 = dict(list03)

# 3. 添加
list02.append("韩辉")
list02.insert(0, "樊世通")

# 4. 定位
# -- 索引
list02[-1] = "老韩"
print(list02[-1])
# -- 切片
# list02[:2] = ["老纪", "老于"]
# ['樊世通', '纪小强', '于全胜', '王琳雅', '老韩']
list02[:2] = "老纪"
print(list02)  # ['老', '纪', '于全胜', '王琳雅', '老韩']

# 　5. 删除
list02.remove("老韩")
del list02[0]  # 删除第一个元素
del list02[-2:]  # 删除后两个元素

# 6. 遍历
# -- 从头到尾
for item in list03:
    print(item)

# 切片产生新列表,浪费内存
# for item in list03[::-1]:
#     print(item)

# -- 通过索引
for i in range(len(list03) - 1, -1, -1):
    print(list03[i])

# (二)字典
# 1. 创建
dict01 = {}
dict_info_of_jxq = {"name": "纪小强", "age": 26, "score": 98}
dict_info_of_yqs = {"name": "于全胜", "age": 25, "score": 93}
dict_info_of_wly = {"name": "王琳雅", "age": 23, "score": 95}

# 2. 字典 --> 列表
list02 = list(dict_info_of_jxq.items())

# 3. 添加
dict_info_of_jxq["sex"] = None

# 4. 定位  容器名[键]
dict_info_of_jxq["name"] = "老纪"
print(dict_info_of_jxq["name"])

# 5. 删除
del dict_info_of_jxq["score"]

a = (10)  # 整数
b = 10, 20, 30  # 元组

# 6. 遍历
# -- 获取所有key      for 键 in 字典名称:
for key in dict_info_of_jxq:
    print(key)
# -- 获取所有value      for 值 in 字典名称.values():
for value in dict_info_of_jxq.values():
    print(value)
# -- 获取所有key 和 value     for 键,值 in 字典名称.items():
for k, v in dict_info_of_jxq.items():
    print(k)
    print(v)
