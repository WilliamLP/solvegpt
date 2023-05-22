from euler import *
primes = sieve(1000000)
print(sum([totient(primes, i) for i in range(2, 1000001)]))
