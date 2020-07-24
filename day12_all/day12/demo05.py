"""
    继承 - 数据
        语法:class 子类(父类):
                def __init__(self,父类参数,子类参数):
                    super().__init__(父类参数)
                    self.子类变量 = 子类参数
"""


# 人 -- 姓名 年龄
# class Person:
#     def __init__(self, name="", age=0):
#         self.name = name
#         self.age = age
#
# # 学生 --
# class Student(Person):
#     pass
#
# # 如果子类没有构造函数,实际父类的构造函数
# s01 = Student("小明",22)
# print(s01.name)
# print(s01.age)

# 人 -- 姓名 年龄
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

# 学生 -- 成绩
class Student(Person):
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score

# 如果子类有构造函数,会覆盖父类构造函数
s01 = Student("小明", 22, 90)
print(s01.name)
print(s01.age)
print(s01.score)
