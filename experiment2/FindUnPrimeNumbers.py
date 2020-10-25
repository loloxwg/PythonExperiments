# 使用filter()函数统计列表中所有非素数
import string
n = int(input("请输入一个大于2的自然数："))
lst = list(range(2, 10))
m = int(n ** 0.5)
for index, value in enumerate(lst):
    if value > m:
        break

    lst[index + 1:] = filter(lambda x: x % value == 0, lst[index + 1:])
print("使用filter()函数统计列表中所有非素数")

print(lst)

print(sorted(set(lst)))

print(set(lst))


