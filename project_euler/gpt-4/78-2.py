def pentagonal_numbers():
    # Generator for pentagonal numbers
    i = 0
    while True:
        i += 1
        yield i*(3*i-1)//2
        if i > 0:
            i = -i
        else:
            i = -i + 1


def partition(n):
    # Dynamic programming approach for partition function
    partitions = [1]
    pentagonal = pentagonal_numbers()
    pent = [next(pentagonal)]
    for i in range(1, n+1):
        j, k = 0, 0
        partitions.append(0)
        while pent[j] <= i:
            partitions[i] += partitions[i - pent[j]] * (-1)**(k//2)
            j += 1
            if j == len(pent):
                pent.append(next(pentagonal))
            k += 1
        partitions[i] %= 10**6  # to avoid overflow
    return partitions[n]


def least_n():
    n = 1
    while True:
        if partition(n) == 0:
            return n
        n += 1


print(least_n())
