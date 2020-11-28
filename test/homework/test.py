import numpy as np

xlist = list(np.random.randint(1, 20, size=20))
print(xlist)
# a = xlist[1::2]  # ji
# print(a)
# b = sorted(xlist[::2], reverse=True)
# print(b)
################### 列表偶数位降序排列No1 ##########
xlist[::2] = sorted(xlist[::2], reverse=True)
print(xlist)
####################列表偶数位降序排列No2 ##########
b = xlist[::2]
b.sort(reverse=True)
xlist[::2] = b
print(xlist)
################################################
# sort()是list的内置函数，只会对原列表操作，无返回值
# 切片具有浅拷贝性质，对列表进行切片得到的是一个新的列表
# 这个时候必须借用b变量来在新列表进行操作
# 错误的示范:
# must assign iterable to extended slice
#     xlist[::2]=xlist[::2].sort()
# TypeError: must assign iterable to extended slice