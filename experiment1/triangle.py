import math
def hypotenuse(a, b):
    return (math.sqrt(a ** 2 + b ** 2))


side1 = int(input("第一条直角边："))
side2 = int(input("第二条直角边："))
print("直角三角形斜边长度为:{}".format(int(hypotenuse(side1, side2))))
