#3-10
import numpy as np
x=list(np.random.randint(1,20,size=20))
print("20个随机数列表\n",x)
a=sorted(x[0:10])
print("前10个元素升序列表\n",a)
b=sorted(x[10:20],reverse=True)
print("后10个元素降序列表\n",b)
