"""
    画出下列代码内存图
    指出打印结果
"""
class MyClass:
    cls_data = 10

    def __init__(self, data):
        self.ins_data = data
        self.ins_data += 5
        MyClass.cls_data += 5


c01 = MyClass(10)
print(c01.ins_data)  # ?
print(MyClass.cls_data)  # ?

c02 = MyClass(10)
print(c02.ins_data)  # ?
print(MyClass.cls_data)  # ?
