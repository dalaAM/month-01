"""
    主模块:入口
        主模块不会生成pyc文件,被导入的模块才会生成.
        pyc文件是源代码到机器码中间的语言,可以加快程序的执行速度.
"""
# import usl
#
# view = usl.StudentView()
# view.main()

# 生成代码快捷键: alt + 回车
from usl import StudentView
# from usl import *

# 保障程序可以按照既定流程执行
if __name__ == '__main__':
    try:
        view = StudentView()
        view.main()
    except:
        print("出错楼")