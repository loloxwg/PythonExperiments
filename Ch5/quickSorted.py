import random


def quickSorted(lst, reverse=False):
    if len(lst) <= 1:
        return lst
    pivot = lst.pop()
    first, second = [], []
    exp = 'x<pivot'

    if reverse == True:
        exp = 'x>=pivot'
    for x in lst:
        if eval(exp):
            first.append(x)
        else:
            second.append(x)
    return quickSorted(first, reverse) + [pivot] + quickSorted(second, reverse)


lst = [random.randint(1, 1000) for i in range(100)]

print(quickSorted(lst, True))


def Sorted(v):
    t = v[::]
    r = []
    while t:
        tt = min(t)
        r.append(tt)
        t.remove(tt)
    return r


def Reverse(v):
    t = v[::]
    r = []

    while t:
        tt = max(t)
        r.append(tt)
        t.remove(tt)
    return r


x = [1, 3, 5, 2, 1, 0, 9, 7]
print(x)
print(Sorted(x))
print(Reverse(x))
