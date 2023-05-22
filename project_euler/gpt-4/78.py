def partitions(n):
    pentagonal = lambda i: i * (3 * i - 1) // 2
    partition = [0] * (n + 1)
    partition[0] = 1

    for i in range(1, n + 1):
        j, k = 1, 1
        while pentagonal(j) <= i:
            partition[i] += partition[i - pentagonal(j)] * k
            if j > 0:
                if j % 2 == 0:
                    j = -j
                else:
                    j = -j + 1
            else:
                if j % 2 == 0:
                    j = -j
                else:
                    j = -j - 1
            if j % 2 == 0:
                k = -1
            else:
                k = 1
    return partition

def least_n_divisible_by_one_million():
    partition = partitions(10)
    for i, p in enumerate(partition):
        if p % 1000000 == 0 and p != 0:
            return i

print(least_n_divisible_by_one_million())
