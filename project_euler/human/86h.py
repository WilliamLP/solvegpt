import math
LIMIT = 100  # Trial and error to get it high enough
count_by_m = [0] * (LIMIT + 1)
for m in range(1, LIMIT + 1):
    for n in range(1, m):  # m > n
        if (m % 2 == n % 2) or math.gcd(m, n) != 1:
            continue
        for k in range(1, LIMIT):
            a = min(k * (m*m - n*n), k * 2*m*n)
            b = max(k * (m*m - n*n), k * 2*m*n)
            if a > LIMIT:
                break

            if a * 2 >= b:  # longest side of the cube is a
                min_small = max(1, b - a)
                max_small = min(b // 2, a)
                count_by_m[a] += max_small - min_small + 1
            if b <= LIMIT:  # longest side of the cube is b
                min_small = 1
                max_small = a // 2
                count_by_m[b] += max_small - min_small + 1

sm = 0
print(sum(count_by_m))
for i, cbm in enumerate(count_by_m):
    sm += cbm
    if sm > 1000000:
        print(i)
        break