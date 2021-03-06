"""
    复习
        数据基本运算
            数据
                变量:操作数据
                    变量名称 = 数据
                        num01 = 250
                        num02 = num01
                        num01 = 300

                核心数据类型:
                    整形 int : 表示整数   250  300          250 + 1 --> 251    可以数学计算
                    浮点型 float:表示小数  2.5  0.0
                    字符串 str:表示文本  "悟空" "250"       "250" + "1" --> "2501"   不能数学计算
                    布尔 bool:表示命题   真True  假False
                    类型转换:
                        结果 = 数据类型(数据)
                        bool(0) --> False
                        bool(0.0) --> False
                        bool("") --> False
                输入输出:
                    -- 输入
                        结果 = input("提示信息")    结果是字符串类型
                        结果 = 数据类型(input("提示信息"))
                    -- 输出
                        print(数据)
                        print("格式" + str(数据))
            运算符
                算数:+ - *  幂运算**  /   //   %
                    5  /  2  --> 2.5 小数商

                    5  // 2  --> 2  整数商
                    5 % 2    --> 1  余数

                    1234 // 1000 -->  1  千位数
                    1234 % 10 --> 4     个位数

                增强:+= -= *=  幂运算**=  /=   //=   %=
                    num = 100
                    num + 10 # 从变量中读取数据进行运算(没有修改)
                    print(num) # 100

                    # num = num + 100   运算过后给自身赋值
                    num += 100

                    print(num) # 110
                比较:==   !=   >  >=   <   <=
                    float(input("请输入你的身价")) > 999999999
                逻辑:and   or   not
                    有钱 and 有房  -->  有钱并且有房
                    有钱 or  有房  -->  有钱或者有房
                    not 有钱 -->  没钱
        语句
            选择语句:有选择性的执行语句
                if 条件:
                    满足条件
                else:
                    不满足条件

                if 条件1:
                    满足条件1
                if 条件2:
                    满足条件2
                else:
                    不满足条件2

                if 条件1:
                    满足条件1
                elif 条件2:
                    不满足条件1,但满足条件2
                else:
                    不满足以上条件

                if 条件1:
                    if 条件2:
                        满足条件1,满足条件2
                    else:
                        满足条件1,不满足条件2

            循环语句:重复执行语句
                while 条件:
                    满足条件

                while True:
                    满足条件
                    if 退出条件:
                        break

                计数器 = 0           --- 循环之前 开始值
                while 计数器 < 10:   --- 循环条件 终止值
                    抄写10遍
                    计数器 += 1      --- 循环内部 更新

            跳转语句:
                break  跳出
"""
