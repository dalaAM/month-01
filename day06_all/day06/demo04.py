"""
    列表推导式
        使用简易方法，将可迭代对象转换为列表。
    exercise:exercise04
"""
# result = []
# for item in range(10):
#     result.append(str(item))
result = [str(item) for item in range(10)]
print(result)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# result = []
# for number in range(20):
#     if number % 2 == 0:
#         result.append(number)
result = [number for number in range(20) if number % 2 == 0]
print(result)

