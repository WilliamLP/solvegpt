from euler import *

LIMIT = 100
prime_partition_counts = defaultdict(int)
def prime_partition_count(n, max_prime_index):
    if n == 1:
        return 0
    if n == 0:
        return 1
    while primes[max_prime_index] > n:
        max_prime_index -= 1
    if max_prime_index == 0:
        return 1 if n % 2 == 0 else 0

    if (n, max_prime_index) not in prime_partition_counts:
        prime_partition_counts[(n, max_prime_index)] = \
            prime_partition_count(n - primes[max_prime_index], max_prime_index) + \
                prime_partition_count(n, max_prime_index - 1)
    return prime_partition_counts[(n, max_prime_index)]

primes = sieve(LIMIT)
pr_index = len(primes) - 1
for n in range(2, LIMIT + 1):
    if prime_partition_count(n, pr_index) > 5000:
        print(n)
        break