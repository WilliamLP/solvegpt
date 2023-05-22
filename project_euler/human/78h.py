
LIMIT = 100000
pentagonals = []
k = 0
while True:
    k += 1
    p1 = k * (3*k - 1) // 2
    if p1 > LIMIT:
        break
    pentagonals.append(p1)

    p2 = k * (3*k + 1) // 2
    if p2 > LIMIT:
        break
    pentagonals.append(p2)


partition_counts = [1,1] + [0] * (LIMIT - 1)
for n in range(2, LIMIT + 1):
    for i, p in enumerate(pentagonals):
        if p > n:
            break
        partition_counts[n] += (1 if i % 4 <= 1 else -1) * partition_counts[n - p]
        partition_counts[n] %= 1000000
    if partition_counts[n] == 0:
        print(n)
        break