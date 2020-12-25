# 内置函数filter()将一个单参数函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象，如果指定函数为None，则返回序列中等价于True的元素。

seq = ['foo', 'x41', '?!', '*********']


def func(x):
    return x.isalnum()  # 测试是否为字母或数字


filter(func, seq)  # 返回filter对象
a = list(filter(func, seq))  # 把filter对象转换为列表

b=list(filter(None,seq))