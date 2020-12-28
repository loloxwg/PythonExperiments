for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0}*{1}={2}'.format(i, j, i * j), end="\n")

a = ['ssss', 'fsfsdfsdfsdf', 'vc', 'a']
for index, value in enumerate(a):
    print('list No.', index + 1, 'is', value, end="\n")

for n in range(100, 1, -1):
    if n % 2 == 0:
        continue
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            break
    else:
        print(n)
        break
