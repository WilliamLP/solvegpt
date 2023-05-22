def sieve(n):
    i = 2
    primes = []
    composites = set()
    while(i < n):
        if i not in composites:
            primes.append(i)
            # Cross out all multiples of i
            j = i + i
            while j < n:
                composites.add(j)
                j += i
        i += (1 if i == 2 else 2)
    return primes

from collections import defaultdict

def prime_factors(primes, n):
    # Factors n and returns a dictionary of {prime factor : multiplicity}
    result = defaultdict(int)
    for pr in primes:
        if pr * pr > n:
            break
        while pr < n and n % pr == 0:
            result[pr] += 1
            n //= pr
    # Than n left must be prime
    result[n] += 1
    return result

primes = sieve(1000000)
triangle, i = 1, 1

while True:
    triangle, i = triangle + (i + 1), i + 1
    factors = prime_factors(primes, triangle)
    num_factors = 1
    for factor, mult in factors.items():
        num_factors *= mult + 1
    print(f'{triangle}: {num_factors}')
    if num_factors > 500:
        break

