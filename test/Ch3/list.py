a = list({'a': 3, 'b': 9, 'c': 78})
print(a)
# 字典的键转列表
b = list({'a': 3, 'b': 9, 'c': 78}.items())
print(b)
# 字典的键值对转列表

print(id({'c': 78}))

x = [3, 5, 7, 9, 11]

print(id(x[1]), id(x[2]), id(x[3]))
# 列表元素地址连续
print(id(x))

# 原地操作
x.append(4)  # 在尾部追加元素
x.insert(0, 2)  # 在指定位置插入元素
x.extend([12, 13, 14])  # 在尾部追加多个元素
print(x)

print(id(x))  # 列表在内存中的地址不变

a = x.pop()  # 弹出并返回尾部元素

print(x, x.pop(), a)

b = x.pop(0)  # 弹出并返回指定位置的元素

print(x, b)

c = x.remove(3)  # 删除首个值为3的元素

print(x, c)

del x[0]  # 删除指定位置上的元素
print(x)

x.clear()  # 删除所有元素

print(x)

# （3）count()、index()
# 列表方法count()用于返回列表中指定元素出现的次数；index()用于返回指定元素在列表中首次出现的位置，如果该元素不在列表中则抛出异常。
x = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
x.count(3)  # 元素3在列表x中的出现次数,#不存在，返回0

x.index(2)  # 元素2在列表x中首次出现的索引,#列表x中没有5，抛出异常
