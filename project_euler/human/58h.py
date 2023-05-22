from euler import *

def next_four_corners(n):
    return [n * n + (n + 1) * i for i in range(4)]

n, count_primes, count_total = 1, 0, 1
while True:
    corners = next_four_corners(n)
    n += 2
    count_primes += len([corner for corner in corners if is_prime(corner)])
    count_total += 4
    if count_primes * 10 < count_total:
        print(n)
        break
