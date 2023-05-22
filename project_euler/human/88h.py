from euler import *

def least_prime_factor(primes, n):
    for pr in primes:
        if n % pr == 0:
            return pr

f_cache = {}
def factorizations(primes, n):  # Returns set of ordered tuples, n not prime
    if n in primes_set:
        return set([(n,)])
    if n not in f_cache:
        pr = least_prime_factor(primes, n)
        prev_fs = factorizations(primes, n // pr)
        new_fs = []
        for f in prev_fs:
            new_fs.append(tuple(sorted(f + (pr,))))
            for i, term in enumerate(f):
                new_fs.append(tuple(sorted(f[:i] + (pr * term,) + f[i+1:])))
        f_cache[n] = set(new_fs)
    return f_cache[n]


LIMIT = 13000
primes = sieve(LIMIT)
primes_set = set(primes)

min_n = [float('inf')] * LIMIT
for n in range(4, LIMIT):
    if n in primes_set:
        continue
    for f in factorizations(primes, n):
        sm = sum(f)
        k = len(f) + (n - sm)
        min_n[k] = min(min_n[k], n)

print(sum(set(min_n[2:12001])))
