# 导入模块,会执行模块的所有代码
import demo01

# 标准库模块
import random

print(random.randint(1,100))
# 模块自身名字
# 1. 模块名称(被导入时)
# 2. __main__(主模块,第一个运行的文件)
print(__name__)


# 导入模块是否成功的唯一标准:
#    导入路径 + sys.path = 真实路径
import sys

# 也可以通过代码,给程序加入根目录.
sys.path.append("/home/tarena/month01/day15/my_project")
print(sys.path)