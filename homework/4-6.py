x = input('Please input an integer less than 1000:')
x = eval(x)
t = x
i = 2
result = []
while True:
    if t == 1:
        break
    if t % i == 0:
        result.append(i)
        t = t / i
    else:
        i += 1

print(x, '=', '*'.join(map(str, result)))