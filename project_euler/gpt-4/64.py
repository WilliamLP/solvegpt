import math

def get_period(n):
    m = 0
    d = 1
    a = a0 = math.isqrt(n)
    period = 0

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1

        if a == 2 * a0:
            break

    return period

count = 0
limit = 10000

for n in range(2, limit + 1):
    r = math.isqrt(n)

    if r * r == n:
        continue

    if get_period(n) % 2 == 1:
        count += 1

print(count)
