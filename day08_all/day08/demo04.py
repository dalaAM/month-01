"""
    函数　-- 设计思想：崇尚小而精,拒绝大而全
    函数　-- 返回值
        def 函数名():
           函数体
           return 数据

        结果　= 函数名()

    定义函数,美元转换为人民币.
"""
# usd = float(input("请输入美元:"))
# rmb = usd * 7.0812
# print(str(usd) + "美元 = " + str(rmb) + " 人民币")

# 转换
def usd_to_rmb(usd):
    rmb = usd * 7.0812
    # 定义函数时　给　调用函数传递　结果
    return rmb

usd = usd_to_rmb(10)
print(usd)


