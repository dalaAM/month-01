"""
    2048 游戏核心算法
"""

list_merge = [2, 0, 2, 0]


# def func01():
#     # 读取
#     print(list_merge)
#     for item in list_merge:
#         print(item)
#     # 读取全局变量,修改列表
#     list_merge[0] = 10
#     # 修改
#     global list_merge
#     list_merge = 0

# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# zero_to_end()
# print(list_merge)


# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
# [2,2,4,8]  --> [4,4,8,0]
def merge():
    """
        合并
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):  # -1：只需要前三个与下一个比较
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


merge()
print(list_merge)

# (选做)day13作业
# 1. 创建全局变量二维列表作为2048地图
map = [
    [2, 0, 0, 2],
    [4, 4, 0, 8],
    [4, 0, 4, 2],
    [8, 2, 2, 0],
]
# 2. 创建函数,向左移动
# 将map中的每行,赋值给全局变量list_merge
# 调用merge函数
# list_merge[0] = 1  # 读取全局变量
# list_merge = 2  # 修改全局变量

# 3. 创建函数，向右移动
# 提示：调用merge实现
