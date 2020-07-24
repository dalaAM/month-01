"""
    实例成员
        实例变量
        实例方法
"""


class Wife:
    def __init__(self, name):
        # 创建实例变量
        self.name = name

    def play(self):
        # 实例方法 可以操作 实例变量
        print(self.name + "玩耍")


w01 = Wife("双儿")
# 修改实例变量
w01.name = "双双"
# 读取实例变量
print(w01.name)
# 通过对象调用实例方法
w01.play()  # 自动传递对象地址 play(w01)
# 通过类名调用实例方法
Wife.play(w01)

# __dict__ python提供的实例变量,存储了对象的实例变量名与值(字典类型)
print(w01.__dict__)

"""
# 不建议:类中/对象的成员,应该在类范围内定义.
class Wife:
    pass


w01 = Wife()
# 　创建实例变量(运行时,由使用者创建实例变量),属于动态语言特征
w01.name = "双儿"
# 　修改实例变量
w01.name = "双双"
# 读取实例变量
print(w01.name)
"""

"""
# 不建议在构造函数外创建实例变量
class Wife:

    def func01(self, name):
        self.name = name


w01 = Wife()
w01.func01("双儿")
# 读取实例变量
print(w01.name)
"""
