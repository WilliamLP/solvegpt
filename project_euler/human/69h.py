from euler import *

primes = sieve(1000000)
best_n, best_ratio = 0, 0
for n in range(2, 1000001):
    tot = 1
    pf = prime_factors(primes, n)
    for p, mult in pf.items():
        tot *= (p ** mult - p ** (mult - 1))
    ratio = n / tot
    if ratio > best_ratio:
        best_n, best_ratio = n, ratio
print(best_n, best_ratio)