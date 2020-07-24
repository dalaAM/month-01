""""
    参照下列代码,定义函数,计算加速度.
    distence = float(input("距离为:"))
    initial_velocity = float(input("速度为"))
    time = float(input("时间为"))
    accelerated_speed = 2 * (distence - initial_velocity * time) / time ** 2
    print("加速度为" + str(accelerated_speed))
"""


def get_accelerated_speed(distence, initial_velocity, time):
    """
        获取加速度
    :param distence: 距离
    :param initial_velocity:初速度
    :param time: 时间
    :return: 加速度
    """
    return 2 * (distence - initial_velocity * time) / time ** 2


print(get_accelerated_speed(100, 5, 2))
