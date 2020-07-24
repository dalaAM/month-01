"""
    循环:重复
        while:根据条件,例如：对折到珠穆朗峰的高度
        for:根据次数,例如:对折36次

    练习1:
        一张纸的厚度是0.01毫米
        请计算，对折多少次超过珠穆朗玛峰(8844.43米).   30 次

    练习2:
        一张纸的厚度是0.01毫米
        请计算，对折36次的高度是多少米.
"""
# 数据:厚度      珠穆朗玛峰     对折次数
# 处理:对折        不超过       计数器
count = 0
# thickness = 0.01 / 1000
# thickness = 0.00001
thickness = 1e-5
while thickness <= 8844.43:
    thickness *= 2
    count += 1
print(count)


thickness = 1e-5
for item in range(36):# 0~35   range(1,37) 1~36
    thickness *= 2
print(thickness)
