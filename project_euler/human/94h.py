
import math
LIMIT = 1000000000

sm = 0
for m in range(2, LIMIT):
    if 2 * m**2 > LIMIT:
        break
    for n in range(1, m):
        if math.gcd(m, n) != 1 or (m % 2 == n % 2):
            continue
        a = min(2*m*n, m*m - n*n)
        b = max(2*m*n, m*m - n*n)
        c = m*m + n*n
        if a + b + c > LIMIT:
            continue
        if abs(2*a - c) == 1:
            perim = 2*a + 2*c
            sm += perim
print(sm)
