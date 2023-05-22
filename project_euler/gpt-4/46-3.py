def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7]:
        if n < p * p:
            return True
        if n % p == 0:
            return False
    for p in range(11, int(n ** 0.5) + 1, 2):
        if n % p == 0:
            return False
    return True

def is_goldbach_false():
    primes = set()
    n = 9  # start from the first odd composite number

    while True:
        if is_prime(n):
            primes.add(n)
        else:  # if n is not prime, it must be composite
            if not any((n - p) in (2 * i ** 2 for i in range(1, int(((n - p) / 2) ** 0.5) + 1)) for p in primes):
                return n  # n cannot be written as the sum of a prime and twice a square
        n += 2  # increment by 2 to get the next odd number

print(is_goldbach_false())
