def josephus(n, k):
    # n代表总人数，k代表报数的数字
    List = list(range(1, n + 1))
    index = 0
    while List:
        temp = List.pop(0)
        index += 1
        if index == k:
            index = 0
            continue
        List.append(temp)
        print(List)
        if len(List) == k-1:
            print(List)
            break


if __name__ == '__main__':
    josephus(100, 3)
