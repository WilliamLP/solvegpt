
import math

counts = [0] * 1500001
for m in range(1, 1300):  # Good enough limit
    for n in range(1, m):  # m > n
        if (m % 2 == n % 2) or math.gcd(m, n) != 1:
            continue
        perimeter = 2*m**2 + 2*m*n
        for p2 in range(perimeter, 1500001, perimeter):
            counts[p2] += 1
print(len([c for c in counts if c == 1]))