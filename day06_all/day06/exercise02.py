"""
    在终端中循环录入内容,如果录入空字符串则停止.
    打印所有录入的内容(字符串)

"""
list_area = []
while True:
    city = input("请输入疫情地区:")
    if city == "":
        break
    list_area.append(city)

result = "-".join(list_area)
print(result)
