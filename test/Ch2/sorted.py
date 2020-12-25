import random

x = list(range(11))
random.shuffle(x)
print(x)
b = sorted(x)
print(b)
a = sorted(x, key=lambda item: len(str(item)), reverse=True)
print(a)

c = sorted(x, key=str)
print(c)

d = ['aaaa', 'bc', 'd', 'ba']
e = sorted(d, key=lambda item: len(str(item)))
# 先按长度排序，长度一样的正常排序
print(e)
f = list(reversed(d))
print(reversed(d))
print(f)
