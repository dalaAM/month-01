"""
    数据基本运算
        数据
            变量:操作数据
            数据类型:字符串str  整数int  小数float
                     "10"       10        10.0
                类型转换: str()    int()    float()
                        结果 = 类型名称(等待转换的数据)
            del:删除变量,数据如果引用计数为0,则被销毁.
        基本运算
            运算符
                算数:+   -  *  **   /   //   %
                    操作两个数字(整数/小数)
                增强:+=   -=  *=  **=   /=   //=   %=
                    增加了对自身赋值的过程
                    a = 10
                    # a + 2 不会改变a的数据
                    a += 2 # a = a + 2

"""
data = "10"
print(data + "1")  # 字符串:一零一
data = 10
print(data + 1)  # 数字:十一

del data