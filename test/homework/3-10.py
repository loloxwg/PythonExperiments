import numpy as np
x=list(np.random.randint(1,20,size=20))
print(x)
a=sorted(x[0:10])
print(a)
b=sorted(x[10:20],reverse=True)
print(b)
