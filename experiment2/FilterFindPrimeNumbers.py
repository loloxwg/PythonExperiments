# find prime numbers
# 实用列表实现筛选法求素数
n = int(input('请输入一个大于2的自然数：'))
lst = list(range(2, n))
m = int(n ** 0.5)
for index, value in enumerate(lst):
    # 如果当前数字已大于最大整数的平方根，结束判断
    if value > m:
        break
    # 对该位置之后的元素进行过滤
    lst[index + 1:] = filter(lambda x: x % value != 0, lst[index + 1:])

print(lst)

# import random
#
#
# def isPrime(n):
#     if n in (2, 3):
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# lst = [random.randint(1, 100) for i in range(50)]
# print(lst)
# print(list(filter(lambda x: isPrime(x) is False, lst)))
# 有点问题这个