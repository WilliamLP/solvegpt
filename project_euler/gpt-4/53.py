import math

count = 0

for n in range(1, 101):
    for r in range(0, n+1):
        if math.comb(n, r) > 1000000:
            count += 1

print(count)
