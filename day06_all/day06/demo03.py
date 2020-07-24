"""
    str --> list
    将一个字符串拆分为多个。
    result = "a-b-c-d".split("-")
    exercise:exercise03

"""
# 语法
result = "a-b-c-d".split("-")
print(result)  # ['a', 'b', 'c', 'd']

# 应用:一个字符串表达多个信息
str_names = "悟空_唐三藏_八戒"
list_names = str_names.split("_")
print(list_names)
