"""
    集合set
        数学计算
"""
set01 = {1, 2, 3}
set02 = {2, 3, 4}

# 交集   "并且"
print(set01 & set02)  # {2, 3}

# 并集   "或者"
print(set01 | set02)  # {1, 2, 3, 4}

# 补集  shift + 6  "补充"
print(set01 ^ set02)  # {1, 4}
print(set01 - set02)  # {1}
print(set02 - set01)  # {4}

# 子集
set03 = {2, 3}
print(set03 < set01) 

