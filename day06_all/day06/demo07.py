"""
    字典
        dict
            key --> value
        新华字典
            拼音 --> 文字
        书店
          书架标签 -->  Python入门到精通
"""
# 1. 创建
# -- 写法1  字典名称 = {键1:值1,键2:值2}
dict01 = {"北京": 593, "上海": 657}
# -- 写法2  字典名称 = dict(格式)    格式 -- > [(k,v),(k,v)]
# 注意:格式的核心思想是能够拆分为键和值
dict02 = dict([("ts", "唐僧"), ("bj", "猪八戒"), ("ss", "沙和尚")])
# dict02 = dict(["唐僧", ("bj", "猪八戒"), ["ss", "沙和尚"]])
print(dict02)  # {'ts': '唐僧', 'bj': '猪八戒', 'ss': '沙和尚'}

# 2. 添加(列表中没有当前key)   字典名称[键] = 值
dict01["黑龙江"] = 944

# 3. 定位 -- 通过键
# 读取
print(dict01["上海"])
# 修改(列表中存在当前key)  字典名称[键] = 值
dict01["北京"] = 594

# 4. 删除
del dict01["黑龙江"]

# 5. 遍历
# -- 获取所有键
for key in dict01:
    print(key)

# -- 获取所有值
for value in dict01.values():
    print(value)

# -- 获取所有键,值
# item 是元组(键,值)
# for item in dict01.items():
#     print(item[0])
#     print(item[1])

# k,v = 元组(键,值)
for k, v in dict01.items():
    print(k)
    print(v)
