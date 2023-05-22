from euler import *

primes = sieve(1000000)
primes_set = set(primes)

for n in range(1, 1000):
    for i in range(len(primes) - n + 1):
        prime_sum = sum(primes[i:i+n])
        if prime_sum >= 1000000:
            break
        if prime_sum in primes:
            print(n, prime_sum)
            break
