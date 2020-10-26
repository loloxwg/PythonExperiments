# 使用filter()函数统计列表中所有非素数
import string
n = int(input("请输入一个大于2的自然数："))
lst = list(range(2, 10))
m = int(n ** 0.5)
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。
# enumerate(sequence, [start = 0])
# sequence -- 一个序列、迭代器或其他支持迭代对象。
# start -- 下标起始位置。
# 返回 enumerate(枚举) 对象。
for index, value in enumerate(lst):
    if value > m:
        break
    lst[index + 1:] = filter(lambda x: x % value == 0, lst[index + 1:])
# python 使用 lambda 来创建匿名函数。
# lambda [arg1 [,arg2,.....argn]]:expression
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# filter(function, iterable)
# function -- 判断函数。
# iterable -- 可迭代对象。
# 返回列表。
print("使用filter()函数统计列表中所有非素数")

print(lst)

print(sorted(set(lst)))

print(set(lst))


