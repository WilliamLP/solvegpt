from euler import *

def sum_of_divisors(n):
    global primes
    return sum(proper_divisors(primes, n))

limit = 28123
primes = sieve(limit)
abundants = [i for i in range(2, limit) if sum_of_divisors(i) > i]
abundant_sums = set()
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s < limit:
            abundant_sums.add(s)
        else:
            break
all_sum = sum([i for i in range(1, limit) if i not in abundant_sums])
print(all_sum)