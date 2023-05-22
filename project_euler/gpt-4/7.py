def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p**2 <= limit:
        if primes[p]:
            for i in range(p**2, limit + 1, p):
                primes[i] = False
        p += 1
    return [x for x in range(2, len(primes)) if primes[x]]

def find_nth_prime(n):
    limit = 5 * n * int(n**(0.5))  # Approximation for upper bound of nth prime
    primes = sieve_of_eratosthenes(limit)
    return primes[n - 1]

nth_prime = find_nth_prime(10001)
print(nth_prime)
