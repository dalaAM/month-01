"""
    5. 斐波那契数列：从第三项开始,每一项都等于前两项之和。
        在终端中获取长度,创建斐波那契数列。
        演示：
            请输入斐波那契数列长度：8
            [1, 1, 2, 3, 5, 8, 13, 21]
"""

length = int(input("请输入斐波那契数列长度："))
# 每一项都等于前两项之和
sequence = [1, 1]
# sequence[2] -->  sequence[1] +  sequence[0]
# sequence[3] -->  sequence[2] +  sequence[1]
# sequence[4] -->  sequence[3] +  sequence[2]
# sequence[n] -->  sequence[n-1] +  sequence[n-2]

# 从索引为2开始 到 长度减1(最大索引)为止
# for n in range(2, length):  # 如果length是5,那么i是2 3 4
#     sequence.append(sequence[n - 1] + sequence[n - 2])

# __ 如果循环体中不使用循环变量,建议使用两个下划线.
# # 需要计算长度-2次(前两个是固定的1)
for __ in range(length - 2):  #length - 2 : 如果列表长度是5,那么需要执行3次(因为前两项是固定的1,1)
    # sequence[-1]倒数第一个 sequence[-2]倒数第二个
    sequence.append(sequence[-1] + sequence[-2])

print(sequence)