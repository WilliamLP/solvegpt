from euler import *

primes = sieve(10 ** 7)
print(f'Generated {len(primes)} primes')
primes_set = set(primes)
for p in reversed(permutations(7)):
    i = int(''.join([str(j + 1) for j in p]))
    if i in primes_set:
        print(i)
        break
