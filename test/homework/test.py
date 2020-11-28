import numpy as np

xlist = list(np.random.randint(1, 20, size=20))
print(xlist)
# a = xlist[1::2]  # ji
# print(a)
# b = sorted(xlist[::2], reverse=True)
# print(b)
b=xlist[::2]
b.sort(reverse=True)
xlist[::2]=b##########   tql   +++++++
# print(c)
print(xlist)