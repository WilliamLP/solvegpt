from euler import *

def is_goldbach_false():
    primes = set()
    squares = set()
    n = 9  # start from the first odd composite number

    while True:
        if is_prime(n):
            primes.add(n)
        else:  # if n is not prime, it must be composite
            if not any((n - p) in squares for p in primes):
                return n  # n cannot be written as the sum of a prime and twice a square
            else:
                squares.update(2 * (n // 2) ** 2 for _ in range(1))

        n += 2  # increment by 2 to get the next odd number

print(is_goldbach_false())
