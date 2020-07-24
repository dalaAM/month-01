"""
    程序产生1个,1到100之间的随机数。
    让玩家重复猜测,直到猜对为止。
    每次提示：大了、小了、恭喜猜对了,总共猜了多少次。

    # 1. 随机数工具
    import random

    # 2. 产生随机数
    num01 = random.randint(1,100)
    num02 = random.randint(1,100)

    print(num01)
"""
import random

random_number = random.randint(1, 100)
count = 1
while True:
    get_number = int(input("请输入要猜的数字（1-100）："))
    if get_number == random_number:
        print("恭喜你才对了,总共猜了" + str(count) + "次")
        break
    elif get_number > random_number:
        print("大了")
    else:
        print("小了")

    count += 1
