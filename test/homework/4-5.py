# x = input()
# xlist = x.split(",")
# xlist = [int(xlist[i]) for i in range(len(xlist))]

import numpy as np
xlist = list(np.random.randint(1, 20, size=20))
print(xlist)
print(xlist[1::2])
print((sorted(xlist[::2], reverse=True)))
print(xlist[1::2] + (sorted(xlist[::2], reverse=True)))
