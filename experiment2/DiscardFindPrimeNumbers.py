# 使用集合实现筛选法求素数
# discard()方法用于移除指定的集合元素。
# 该方法不同于remove()方法，因为
# remove()方法在移除一个不存在的元素时会发生错误，
# 而discard()方法不会
n = int(input("请输入一个大于2的自然数："))
a_set = set(i for i in range(2, n + 1))

for i in range(2, int(n ** 0.5) + 1):
    for j in range(i + 1, n + 1):
        if j % i == 0:
            a_set.discard(j)

print(a_set)
