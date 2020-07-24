"""
    画出下列代码内存图
"""

list_devices01 = ["存储器", "控制器", "运算器"]
# 将右侧列表地址赋值给第一个元素
list_devices01[0] = ["内存", "硬盘"]

list_devices02 = ["控制器", "运算器", "存储器"]
# 切片修改,左右容器长度可以不一致
# 遍历右侧列表元素（２个） 依次赋值给左侧定位的区域(１个)
list_devices02[0:1] = ["内存", "硬盘"] #[ '内存', '硬盘', '运算器', '存储器']
# 遍历右侧列表元素（1个） 依次赋值给左侧定位的区域(3个)
list_devices02[1:] = ["cpu"]# ['内存', 'cpu']

print(list_devices01)# [['内存', '硬盘'], '控制器', '运算器']
print(list_devices02)# ['内存', 'cpu']
