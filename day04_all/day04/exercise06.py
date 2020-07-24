"""
    练习１：
    在终端中录入一个内容,循环打印每个文字的编码值。

    练习２：
    循环录入编码值,打印文字.直到输入空字符串,停止。　
"""
get_chr = input("请输入字符串：")
for item in get_chr:
    print(ord(item))

# get_value = input("请输入数字:")
# while get_value != "":
#     char = chr(int(get_value))
#     print(char)
#     get_value = int(input("请输入数字"))

while True:
    get_value = input("请输入数字:")
    if get_value == "":
        break
    char = chr(int(get_value))
    print(char)
