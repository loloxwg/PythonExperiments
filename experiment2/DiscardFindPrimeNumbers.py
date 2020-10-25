# 使用集合实现筛选法求素数

n = int(input("请输入一个大于2的自然数："))
a_set = set(i for i in range(2, n + 1))

for i in range(2, int(n ** 0.5) + 1):
    for j in range(i + 1, n + 1):
        if j % i == 0:
            a_set.discard(j)

print(a_set)
