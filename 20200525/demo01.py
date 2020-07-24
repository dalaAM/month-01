'''
python 自动化内存管理机制
    1.引用计数  每个对象 记录被变量绑定的次数 当为0时  销毁
        缺点：列表循环引用
          即使两个列表都是垃圾 也不会被销毁 因为引用都是1
    2.标记清除 扫描全部内存 标记没用的数据
        缺点：全盘扫描 性能消耗过大
    3.分代回收
          新创建的对象 会放在‘年轻代’内存中
          本代空间存满以后 会进行升代操作（标记清除 将可用的数据移动到下一代）

    4.价值 尽可能少的产生垃圾 对象池 设置分代回收
    小整数池：-5~256范围的整数会存在内存中不释放
'''
# a = [10]
# a = None
#
# list01 = []
# list02 = []
# list01.append(list02)
# list02.append(list01)
# del list01
# del list02

# str_res = ''
# for i in range(10):
#     str_res += str(i)
# print(str_res)

# str_res = []
# for i in range(10):
#     str_res.append(str(i))
# print(str_res)

#对象池 每次创建对象 先判断池中是否有对应的对象存在 如果存在就返回地址 否则再开辟空间
#提高内存利用率 相同的对象只保存一次
# data01 = 1.12345
# data02 = 1.12345
# print(id(data01))
# print(id(data02))

# list01 = [1,2,3]
# list02 = list01
# list02[0] = 'A'
# print(list01)

# list02 = list01[:]
# list02[0] = 'A'
# print(list01)


def fun01():
    for item in range(10):
        yield item

# for item in fun01():
#     print(item)

#生成器 转  列表
#惰性操作 转 立即操作
#省内存      操作灵活
#生成器缺点  从头到尾取一次数据
list01 = list(fun01())
print(list01)