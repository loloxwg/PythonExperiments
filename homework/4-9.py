# 分段函数计算
def fun(x):
    if x < 0:
        y = 0
    elif 0 < x < 5:
        y = x
    elif 5 <= x < 10:
        y = 3 * x - 5
    elif 10 <= x < 20:
        y = 0.5 * x - 2
    elif x >= 20:
        y = 0
    print("y = ", y)


x = int(input("输入x"))
fun(x)
