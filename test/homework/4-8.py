# 输出1，2，3，4组成的所有素数
#
import itertools


#
# a = [1, 2, 3, 4]
#
# print(list(itertools.permutations(a, 4)))
#
# comb = itertools.permutations("1234", 4)
# for x in comb:
#     ''.join(x)
#
# print(x)


def find_primer(lst):
    # n = int(input('请输入一个大于2的自然数：'))
    # lst = list(range(2, n))
    m = int(4321 ** 0.5)
    for index, value in enumerate(lst):
        # # 如果当前数字已大于最大整数的平方根，结束判断
        # if index >m :
        #     break
        # # 对该位置之后的元素进行过滤
        # lst[index + 1:] = filter(lambda x: x % 2 != 0, lst[index + 1:])
        lst= filter(lambda x: x % value != 0, list(range(2,value)))
    print(lst)


a = list(map("".join, itertools.permutations('1234')))
a = [int(a[i]) for i in range(len(a))]

print(a)

find_primer(a)
