def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p**2 <= limit:
        if primes[p]:
            for i in range(p**2, limit + 1, p):
                primes[i] = False
        p += 1
    return primes

def sum_primes_below_n(n):
    sieve = sieve_of_eratosthenes(n)
    prime_sum = 0
    for p in range(2, n):
        if sieve[p]:
            prime_sum += p
    return prime_sum

n = 2000000
result = sum_primes_below_n(n)
print(result)
