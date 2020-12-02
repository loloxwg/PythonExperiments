# 输出1，2，3，4组成的所有素数
#
import itertools


def isprimer(value):
    for j in range(3, value):
        if value % j == 0:
            return 0
            break
        else:
            if j == value - 1:
                return value
                continue


a = list(map("".join, itertools.permutations('1234')))
a = [int(a[i]) for i in range(len(a))]
b = []

for i in a:
    if isprimer(i) != 0:
        b.append(isprimer(i))

print(b)

# find_primer(a)
