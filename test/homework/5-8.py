# 多整数输出最值与和
import numpy as np
xlist=list(np.random.randint(1,20,size=20))
xlist=[int(xlist[i]) for i in range(len(xlist))]
def max_and_sum(*lst):
    print("最大值:",max(lst))
    print("求和:",sum(lst))

max_and_sum(*xlist)

