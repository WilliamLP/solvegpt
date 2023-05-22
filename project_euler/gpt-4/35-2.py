def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for index, is_prime in enumerate(primes):
        if is_prime:
            for multiple in range(index * index, limit + 1, index):
                primes[multiple] = False
    return [i for i, prime in enumerate(primes) if prime]

def rotations(n):
    str_n = str(n)
    return [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]

def is_circular_prime(primes, n):
    return all(rot in primes for rot in rotations(n))

primes = set(sieve_of_eratosthenes(1000000))
primes.discard(2)
primes.discard(5)

circular_primes = [2, 5]  # Include 2 and 5 as they are circular primes
for prime in primes:
    if not any(digit in {'0', '2', '4', '5', '6', '8'} for digit in str(prime)):
        if is_circular_prime(primes, prime):
            circular_primes.append(prime)

print(len(circular_primes))
