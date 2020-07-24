def func01(*args, **kwargs):
    print(args)
    print(kwargs)


func01()
func01(1, 2, 3)
func01(a=1, b=2)
func01(1, 2, 3, a=1, b=2)


# func01(1,2,a=1,3,b=2)


def func02(p1, p2, *args, p3, p4=4):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(p4)


func02(1, 2, p3=3)
func02(1, 2, 3, 4, 5, p3=3, p4=5)


# 必填1个
def func03(list01):
    print(list01)


# 位置实参不定长
def func04(*args):
    print(args)


func03(1)
func03([1, 2, 3, 4])
func03({"a": 1, "b": 2})

func04(1)
func04([1, 2], [3, 4])
func04({"a": 1, "b": 2})
