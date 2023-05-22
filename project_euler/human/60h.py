from euler import *
limit = 100000000
primes_set = set(sieve(limit))
print('done sieve')
small_primes = [p for p in primes_set if p < 10000]

def test_prime_pair(p1, p2):
    i1 = int(str(p1) + str(p2))
    i2 = int(str(p2) + str(p1))
    return i1 in primes_set and i2 in primes_set

prime_groups_by_size = []
prime_groups_by_size.append(set([(p,) for p in small_primes]))
for i in range(1, 5):
    print('Loop iteration', i)
    prime_groups_by_size.append(set())
    for prev_group in prime_groups_by_size[i - 1]:
        for prime in small_primes:
            if any([prime <= prev_prime for prev_prime in prev_group]): # Only generate ascending
                continue
            if all([test_prime_pair(prime, prev_prime) for prev_prime in prev_group]):
                prime_groups_by_size[i].add(prev_group + (prime,))
print(prime_groups_by_size[4])

best_sum = float('inf')
for prime_group in prime_groups_by_size[4]:
    best_sum = min(best_sum, sum(prime_group))
print(best_sum)


