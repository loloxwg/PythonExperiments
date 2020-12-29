import time
import random

x = [random.randint(0, 100) for i in range(1000)]
d = set(x)
for v in d:
    print(v, ':', x.count(v))

# 也可以直接使用字典来实现该功能，并且获得更高的执行效率


listRandom = [random.randint(1, 100) for i in range(1000)]

d = dict()

start = time.time()

for i in x:  # 对随机数列表扫描一次，即可得到结果

    d[i] = d.get(i, 0) + 1

print(time.time() - start)
print(d)
