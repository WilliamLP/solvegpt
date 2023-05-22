
import math
count = 0
for d in range(2, 12001):
    for n in range(d // 3 + 1, (d + 1) // 2):
        if math.gcd(d, n) > 1:
            continue
        count += 1
print(count)
