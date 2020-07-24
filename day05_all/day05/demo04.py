"""
    列表 list
    exercise:exercise03~06
"""
# 1. 创建列表
# -- 写法1   列表名 = [元素1, 元素2]
list_names = ["林恺", "柯良", "王琳雅"]
# -- 写法2   列表名 = list(容器)
list_numbers = list(range(6))  # [0, 1, 2, 3, 4, 5]
list01 = list("我是齐天大圣孙悟空")  # ['我', '是', '齐', '天', '大', '圣', '孙', '悟', '空']

# 2. 添加元素
# -- 写法1  列表名.append(元素)
list_names.append("刘硕")
# -- 写法2 列表名.insert(插入的索引,元素)
list_names.insert(2, "李自强")

# 3. 定位元素
print(list_names)  # ['林恺', '柯良', '李自强', '王琳雅', '刘硕']
# -- 索引:单个元素
print(list_names[2])  # 读取第三个元素
list_names[2] = "强强"  # 修改第三个元素

# -- 切片:多个元素
# $通过切片获取元素,会产生新容器
print(list_names[-3:])  # 读取后三个元素['李自强', '王琳雅', '刘硕']
# $遍历右侧容器,依次为左侧定位的元素赋值
list_names[-3:] = ["老李", "老王", "老刘"]  # 修改后三个元素
print(list_names)

# 4. 删除元素
# -- 根据定位删除
#     del 列表名称[索引]
#     del 列表名称[切片]
del list01[2]  # 删除list01中第三个元素
del list01[-3:]  # 删除list01中最后三个元素
# -- 根据元素删除
# remove 内部会从头到尾进行查找,删除第一个匹配项
list01.remove("天")
# 如果不知道元素是否存在,先通过in判断
if "你" in list01:
    list01.remove("你")

# 5. 遍历列表
# -- 从头到尾依次获取全部元素
for name in list_names:
    print(name)

# -- 索引
# 从前向后跳着获取元素
for i in range(0, len(list_names), 2):  # i : 0 2 4
    print(list_names[i])

# 从后向前获取所有元素 4 3 2 1 0
# 开始: len(list_names) - 1
# 结束:-1, 不会包含-1,会获取上一个(0)
# 间隔:-1, 倒序
for i in range(len(list_names) - 1, -1, -1):  # 4 3 2 1 0
    # print(i) # 不是打印索引
    print(list_names[i])
