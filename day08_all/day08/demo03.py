"""
    将下列代码,定义为函数.
    for r in range(2):  # 行数        0      1
        for c in range(5):  # 列数  01234  01234
            print("老王", end=" ")
        print()  # 换行

"""


def print_table(data, r_count, c_count):
    for r in range(r_count):  # 行数
        for c in range(c_count):  # 列数
            print(data, end=" ")
        print()  # 换行


print_table("老王", 2, 5)
print_table("老崔", 6, 3)
