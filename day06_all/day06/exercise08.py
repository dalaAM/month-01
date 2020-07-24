"""
    练习1:创建三个字典,存储前三个地区疫情信息(名称,新增,现有,累计,治愈)
    练习2:为以上三个字典,添加si亡信息
    练习3:将第二个字典的新增人数设置为0,
    练习4:打印第二个字典信息:
        格式:  xx新增xx,现有xx,累计xx,治愈xx,si亡xx
"""
# 练习1:创建三个字典,存储前三个地区疫情信息(名称,新增,现有,累计,治愈)
hlj = {"city": "黑龙江", "now": 116, "cofirmed": 138, "total": 944, "cure": 815}
hk = {"city": "香港", "now": 80, "cofirmed": 104, "total": 1040, "cure": 960}
tw = {"city": "台湾", "now": 79, "cofirmed": 95, "total": 440, "cure": 355}

# 练习2:为以上三个字典,添加si亡信息
hlj["death"] = 13
hk["death"] = 4
tw["death"] = 6

# 练习3: 将第二个字典的新增人数设置为0,
hk["now"] = 0

# 练习4: 打印第二个字典信息:
# 格式: xx新增xx, 现有xx, 累计xx, 治愈xx, si亡xx
print("%s新增%d,现有%d,累计%d,治愈%d,si亡%d" % (hk["city"], hk["now"], hk["cofirmed"], hk["total"], hk["cure"], hk["death"]))
