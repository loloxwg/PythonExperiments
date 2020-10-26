def dem2(a, n):
    a = str(a)
    # str() 函数将对象转化为适于人阅读的形式。返回一个对象的string格式。
    # a->'a'
    result = sum(eval(a * i) for i in range(1, n + 1))

    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    # 'a'*1='a'
    # 'a'*2='aa'
    # sum()方法对序列进行求和计算。返回计算结果。

    return result


print(dem2(3, 4))


def dem1(k, n):
    result, t = 0, 0
    for i in range(1, n + 1):
        t = t * 10 + k
        result = result + t
    return result


print(dem1(3, 4))

# def demo(v, n):
#     assert type(n) == int and 0 < v < 10, 'v must be integer between 1 and 9'
#     result, t = 0, 0
#     for i in range(10):
#         t = t * 10 + v
#         result = result + t
#     return result
#
#
# print(demo(3, 4))

