"""
    练习1:
        创建列表,存储前3个疫情地区名称
        创建列表,存储前3个现有确诊人数
        创建列表,存储前3个疫情累计人数
    练习2:
        为练习1的三个列表,追加第4个信息.
        为练习1的三个列表,将北京信息插入到第1个位置.
"""
# 　存储前3个疫情地区名称
list_city = ["黑龙江", "香港", "台湾"]
# 存储前3个现有确诊人数
list_cofirmed = [138, 104, 95]
# 存储前3个疫情累计人数
list_total = [944, 1040, 440]

# 为练习1的三个列表,追加第4个信息.
list_city.append("陕西")
list_cofirmed.append(39)
list_total.append(308)

# 为练习1的三个列表,将北京信息插入到第1个位置.
list_city.insert(0, "北京")
list_cofirmed.insert(0, 27)
list_total.insert(0, 593)
