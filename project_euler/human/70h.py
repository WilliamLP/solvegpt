from euler import *
primes = sieve(10000000)
best_r = 999
for n in range(2, 10000001):
    t = totient(primes, n)
    if sorted(str(n)) == sorted(str(t)):
        r = n / t
        if r < best_r:
            best_r = r
            print(n, t, n / t)