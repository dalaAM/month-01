"""
    六大原则
        迪米特:低耦合,找个爸爸隔离变化.
        里氏替换:爸爸出现的地方,儿子可以替换掉.
                 形参爸爸类型   实参儿子对象

                重写的时候,尽量super().爸爸的方法()
"""

class EmployeeManager:

    def __init__(self):
        self.list_employees = []

    # 形参:爸爸(父类类型)
    def add_employee(self, emp):
        self.list_employees.append(emp)

    def calculate_total_salary(self):
        total_salary = 0
        for emp in self.list_employees:
            # 编写代码时:调用的是爸爸(员工类)
            # 运行代码时:执行的是儿子(程序员/测试员...)
            total_salary += emp.get_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        """
            计算薪资方法
        :return: 该员工的薪资
        """
        return self.base_salary

# ------------------------------------------------
class Programmer(Employee):

    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self):
        # 扩展重写:重写时,先调用父类方法,再进行补充.
        # return self.base_salary +  self.bonus
        return super().get_salary() + self.bonus

class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_salary(self):
        # return self.base_salary + self.bug_count * 5
        return super().get_salary() + self.bug_count * 5

manager = EmployeeManager()
# 实参:儿子(程序员)
manager.add_employee(Programmer(10000, 100000))
manager.add_employee(Tester(8000, 100))
print(manager.calculate_total_salary())
