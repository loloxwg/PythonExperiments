# x = input()
# xlist = x.split(",")
# xlist = [int(xlist[i]) for i in range(len(xlist))]

import numpy as np

xlist = list(np.random.randint(1, 20, size=20))
print(xlist)
a = xlist[1::2]  # ji
print(a)


c=[]
b = sorted(xlist[::2], reverse=True)
print(b)
c=xlist[::2]
c.sort(reverse=True)
print(c)
print(xlist)


# print(xlist[1::2] + (sorted(xlist[::2], reverse=True)))
