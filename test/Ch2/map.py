a = list(map(str, range(5)))


# 把单参数函数映射到一个序列的所有元素
def add5(v):  # 单参数函数

    return 5 + v


b = list(map(add5, range(5)))


# 把双参数函数映射到两个序列上

def add(x, y):
    return x + y  # 可以接收2个参数的函数


c = list(map(add, range(5), range(5, 10)))


# 自定义函数
def myMap(iterable, op, value):
    if op not in "+-*/":  # 实现序列与数字的四则运算
        return "Error operator"
    func = lambda i: eval(repr(i) + op + repr(value))
    return map(func, iterable)


# repr(i)返回一个对象的 string 格式。
d = list(myMap(range(5), "+", 5))
e = list(myMap(range(6), "-", 8))

import random

x = random.randint(1, 1e30)
print(x)
f = list(map(int, str(x)))
