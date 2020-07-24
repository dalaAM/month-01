# 梯形面积： （上底 + 下底) * 高  / 2

# 获取数据
top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
# 逻辑计算
result = (top_base + bottom_base) * height / 2
# 显示结果
print("梯形面积是：" + str(result))