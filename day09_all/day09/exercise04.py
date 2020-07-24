"""
    定义函数,根据小时、分钟、秒,计算总秒数
    调用：提供小时、分钟、秒
    调用：提供分钟、秒
    调用：提供小时、秒
    调用：提供分钟
"""

def calculate_total_times(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second


print(calculate_total_times(1, 2, 3))
# print(calculate_total_times(0, 2, 3))
print(calculate_total_times(minute=2, second=3))
# print(calculate_total_times(1, 0, 3))
# print(calculate_total_times(hour=1, second=3))
print(calculate_total_times(1, second=3))
# print(calculate_total_times(0, 2, 0))
print(calculate_total_times(minute=2))
