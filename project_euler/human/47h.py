from euler import *

primes = sieve(1000000)
streak = 0
for i in range(2, 1000000):
    pf = prime_factors(primes, i)
    if len(pf.keys()) == 4:
        streak += 1
    else:
        streak = 0
    if streak == 4:
        print(i - 3)
        break