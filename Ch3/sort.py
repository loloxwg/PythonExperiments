import random
# sort()、reverse()
# 列表对象的sort()方法用于按照指定的规则对所有元素进行排序；reverse()方法用于将列表所有元素逆序或翻转。

x = list(range(11))  # 包含11个整数的列表
random.shuffle(x)  # 把列表x中的元素随机乱序
print("x:把列表x中的元素随机乱序", x)
print("x地址sort前:", id(x))
x.sort(key=lambda item: len(str(item)), reverse=True)  # 按转换成字符串以后的长度
print("x地址sort后:", id(x))
print("x:按转换成字符串以后的长度,降序排序", x)

x.sort(key=str)
print("按转换为字符串后的大小，升序排序", x)

x.sort()
print('按默认规则排序', x)

x.reverse()
print('把所有元素翻转或逆序', x)
