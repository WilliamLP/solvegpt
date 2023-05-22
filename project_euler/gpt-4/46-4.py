import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_composite(n):
    while True:
        n += 2
        if not is_prime(n):
            return n

n = 9
while True:
    n = next_composite(n)
    goldbach = False
    for x in range(1, math.isqrt(n // 2) + 1):
        if is_prime(n - 2 * x * x):
            goldbach = True
            break
    if not goldbach:
        print(n)
        break
