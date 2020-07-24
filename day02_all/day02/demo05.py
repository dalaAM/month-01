"""
    核心数据类型
        不同数据类型,行为不同.
            int    -->  二进制
            float  -->  二进制
            str    -->  二进制 
"""
# 主干
# 1. 字符串str
name = "刘新成"
# 2. 整形int:整数
age = 18
# 3. 浮点型float:小数
money = 2.5

# 4. 整形int字面值:不同情境下,使用不同进行.
# 　-- 十进制DEC：每位用十种状态计数，逢十进一，写法是0~9。
# 0 1  2   3   4     5  .....  7    8   9   10    11 ....
number01 = 10
# 　-- 二进制BIN：每位用二种状态计数，逢二进一，写法是0/1。
# 0 1 10  11  100   101 .....
number02 = 0b10
# 　-- 八进制OCT:每位用八种状态计数，逢八进一，写法是0~7。
# 0 1 2      ....             7    10   11  ....
number03 = 0o10
# 　-- 十六进制HEX:每位用十六种状态计数，逢十六进一，写法是0~9,A~F。
# 0 1 2      ....                          A      B ...
number04 = 0x10

print(number01)  # 10
print(number02)  # 2
print(number03)  # 8
print(number04)  # 16

# 5. 浮点型字面值
number05 = 0.000000000000000000000000000000001
# 科学计数法 1 * 10 -5
print(number05)# 1e-33