import math


def isPrime(x):
    n = int(math.sqrt(x) + 1)
    for i in range(2, n):
        if x % i == 0:
            return 'False'
    else:
        return 'True'


print(isPrime(4))
