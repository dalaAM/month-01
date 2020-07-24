"""
3. 使用IterableHelper完成下列功能
        list01 = [3,43,4,56,6,76,87,9]
        -- 在list01中找出所有大于10的数字
        -- 在list01中找出第一个偶数
        -- 在list01中找出最大的数字
        -- 对list01进行升序排列
"""
from common.iterable_tools import IterableHelper

list01 = [3, 43, 4, 56, 6, 76, 87, 9]
for item in IterableHelper.find_all(list01, lambda number: number > 10):
    print(item)

result = IterableHelper.find_single(list01, lambda number: number % 2 == 0)
print(result)

result = IterableHelper.get_max(list01, lambda number: number)
print(result)

IterableHelper.order_by(list01,lambda number: number)
print(list01)