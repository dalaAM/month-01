"""
    复习
        循环
            while:满足条件重复执行,例如:折纸到珠穆朗峰的高度
            for:遍历容器,例如:获取字符串中的每个字符
            for+range:根据次数重复,例如:折纸36次

        跳转
            break
            continue

"""
# for item in range(10):  # 0~9
#     # print("执行第" + str(item) + "次")
#     # print("执行第%d次" % (item))
#     print(f"执行第{item}次")

for number in range(10):
    if number % 2 == 0:
        # continue
        break
    print(number)

# for number in range(10):
#     if number % 2 != 0:
#         print(number)
