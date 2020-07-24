"""
    可迭代对象的工具箱
"""

"""
    精通函数式编程  
        在实际项目中，根据需求实现了各种功能。 但是很多功能主体部分相同，只是核心算法不同。
        将多个功能的主体部分,也就是通用代码定义到IterableHelper类中。
        将不同的核心算法使用函数类型的形参隔离，将不同算法通过lambda表达式传递进来。
        这个思想，与面向对象编程是异曲同工。
        ....
"""


class IterableHelper:
    """
        可迭代对象助手类:负责定义对可迭代对象的常用操作
    """

    @staticmethod
    def find_all(list_target, func):
        """

        :param list_target:
        :param func:
        :return:
        """
        for item in list_target:
            # if item.price > 10000:
            if func(item):
                yield item

    @staticmethod
    def find_single(list_target, func):
        for item in list_target:
            if func(item):
                return item

    @staticmethod
    def get_count(list_target, func):
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count

    @staticmethod
    def select(list_target, func):
        for item in list_target:
            yield func(item)

    @staticmethod
    def get_max(list_target, func):
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(max_value) < func(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def get_min(list_target, func):
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(min_value) > func(list_target[i]):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def order_by(list_target, func):
        for r in range(len(list_target) - 1):
            for c in range(r + 1, len(list_target)):
                if func(list_target[r]) > func(list_target[c]):
                    list_target[r], list_target[c] = list_target[c], list_target[r]
