def pentagonal_numbers():
    i = 0
    while True:
        i += 1
        yield i*(3*i-1)//2
        if i > 0:
            i = -i
        else:
            i = -i + 1


def partition(n, partitions):
    pentagonal = pentagonal_numbers()
    pent = [next(pentagonal)]
    for i in range(len(partitions), n+1):
        j, k = 0, 0
        partitions.append(0)
        while pent[j] <= i:
            partitions[i] += partitions[i - pent[j]] * (-1)**(k//2)
            partitions[i] %= 10**6  # to avoid overflow
            if partitions[i] == 0:  # if it's divisible by 10^6, break
                break
            j += 1
            if j == len(pent):
                pent.append(next(pentagonal))
            k += 1
    return partitions[n]


def least_n():
    n = 1
    partitions = [1]  # keep track of previously computed partitions
    while True:
        if partition(n, partitions) == 0:
            return n
        n += 1


print(least_n())
