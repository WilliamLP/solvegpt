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

print(sieve(1000000)[10000])