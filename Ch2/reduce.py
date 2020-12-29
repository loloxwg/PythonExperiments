from functools import *

# 标准库functools中的函数reduce()可以将一个接收2个参数的函数以迭代累积的方式从左到右依次作用到一个序列或迭代器对象的所有元素上，并且允许指定一个初始值
seq = list(range(1, 10))

a = reduce(lambda x, y: x + y, seq)

print(a)

import operator

operator.add(3, 5)

b = reduce(operator.add, seq)

c = reduce(operator.mul, seq)

e = reduce(operator.mul, range(1, 6))#阶乘

f = reduce(operator.add, map(str, seq))

g = reduce(operator.add, [[1, 2], [3]], [])
