"""
    容器通用操作 -- 以字符串为例
    exercise:exercise01
"""
# + 用于拼接两个容器
name = "悟空"
name += "八戒"
print(name)  # 悟空八戒

# * 重复生成容器元素
name = "悟空"
name *= 72
print(name)  #

# < <= > >= == !=：依次比较两个容器中元素,一但不同则返回比较结果。
print("孙悟空" > "猪八戒")

# in 成员运算  如果在指定的序列中找到值，返回bool类型。
print("是齐" in "我是齐天大圣孙悟空")