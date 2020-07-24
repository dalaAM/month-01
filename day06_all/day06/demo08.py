"""
    列表擅长存储一个维度信息
        例如:疫情地区名称
            list_city = ["黑龙江", "香港", "台湾"]
            确诊人数
            list_cofirmed = [138, 104, 95]
            累计人数
            list_total = [944, 1040, 440]
    字典擅长存储多个维度信息
        例如:黑龙江疫情信息
            hlj = {"city": "黑龙江", "cofirmed": 138, "total": 944}
    exercise:exercise08
"""
# 列表存储多个维度信息
# hlj = ["黑龙江", 138, 944]
# print("地区名称:" + hlj[0])
# print("确诊人数:" + str(hlj[1]))
# print("累计人数:" + str(hlj[2]))
# 代码可读性差: 0 --> 地区名称    1 --> 确诊人数   2 --> 累计人数

hlj = {"city": "黑龙江", "cofirmed": 138, "total": 944}
print("地区名称:" + hlj["city"])
print("确诊人数:" + str(hlj["cofirmed"]))
print("累计人数:" + str(hlj["total"]))
# 代码可读性强: city --> 地区名称    cofirmed --> 确诊人数   total--> 累计人数


