"""
    属性: 保护实例变量
        本质思想: 拦截对实例变量的操作,转换为对私有变量的操作
        注意:属性名必须与实例变量名相同

    @property
    def 属性名(self):
        return self.__属性名

    @age.setter
    def age(self, value):
        if 条件:
            self.__属性名 = value
        else:
            raise Exception(提示信息) # 产生错误
    exercise:
      创建敌人类
        创建实例变量并保证数据在有效范围内
            姓名、血量、攻击力、防御力
                  0-100  1 – 30、 0 – 20
"""


# 需求: 保护数据,在有效范围内.
# 保障老婆的年龄在22到100之间

class Wife:
    def __init__(self, name="", age=0):
        # 快捷键: alt + 回车 --> 自动生成代码
        self.name = name
        self.age = age  # 调用def age(self, value)方法 age(25)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 100:
            self.__age = value
        else:
            raise Exception("超过结婚年龄")  # 产生错误


w01 = Wife("双儿", 25)
w01.age = 23
print(w01.age)  # 调用def age(self)方法
