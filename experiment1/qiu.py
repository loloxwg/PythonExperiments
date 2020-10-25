import math

r = float(input("请输入半径："))

sarea = 4 * math.pi * r * r
volume = 4 / 3 * math.pi * r ** 3

print("球的表面积: %10.2f" % sarea)
print("球的体积: %10.2f" % volume)
