# 输出1，2，3，4组成的所有素数

import itertools
def IsPrime(p):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(p ** 0.5) + 1, 2):
        if p % i == 0:
            return False
    return True

a = list(map("".join, itertools.permutations('1234')))
a = [int(a[i]) for i in range(len(a))]
# print(a)
b = []
for i in a:
    if IsPrime(i):
        b.append(i)
print("1234组成的所有素数",b)
