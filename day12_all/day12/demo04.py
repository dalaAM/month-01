"""
    内置函数
        isinstance(对象, 类型)
        返回指定对象是否是某个类的对象。
        issubclass(类型，类型)
        返回指定类型是否属于某个类型。
"""


class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


p01 = Person()
s01 = Student()

# 对象 vs 类型
# 人对象 是一种 人类型
print(isinstance(p01, Person))  # True
# 学生对象 是一种 人类型
print(isinstance(s01, Person))  # True
# 学生对象 是一种 老师类型
print(isinstance(s01, Teacher))  # False
# 人对象 是一种 学生类型
print(isinstance(p01, Student))  # False

# 类型 vs 类型
# 人类型 是一种 人类型
print(issubclass(Person, Person))  # True
# 学生类型  是一种 人类型
print(issubclass(Student, Person))  # True
# 学生类型 是一种 老师类型
print(issubclass(Student, Teacher))  # False
# 人类型 是一种 学生类型
print(issubclass(Person, Student))  # False

# 是     是一种
print(type(p01) == Person)  # True
# 学生对象 是  人类型
print(type(s01) == Person)  # False
# 学生对象 是  老师类型
print(type(s01) == Teacher)  # False
# 人对象 是  学生类型
print(type(p01) == Student)  # False
