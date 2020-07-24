"""
    继承 - 行为
        财产:钱不用儿子挣,但是可以花.
        皇位:江山不用太子打,但是可以坐.
        编程:代码不用子类写,但是可以用.
        语法:
            class 儿子(爸爸):
                ...
"""


# 多个类有相同成员,且 概念统一(多个类都是一种类).
# 1. 学生 -- 学习 说话
#    老师 -- 教学 说话
# class Student:
#     def study(self):
#         print("学习")
#
#     def say(self):
#         print("说话")
#
# class Teacher:
#     def teach(self):
#         print("教学")
#
#     def say(self):
#         print("说话")

# 多个类有相同成员,且 概念统一(多个类都是一种类).
# 1. 学生 -- 学习 说话
#    老师 -- 教学 说话
class Person:
    def say(self):
        print("说话")


class Student(Person):
    def study(self):
        print("学习")
        self.say()


class Teacher(Person):
    def teach(self):
        print("教学")
        # 建议:子类通过super()调用父类成员
        super().say()


s01 = Student()
s01.study()  # 调用自身方法
s01.say()  # 调用父类方法


