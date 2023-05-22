import math

def is_prime(n):
    """Check if a number is a prime number."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def first_spiral_below_ratio(ratio):
    """Find the side length of the spiral where the ratio of primes on the diagonals first falls below a given ratio."""
    primes = 0
    total = 1  # counting the center of the spiral
    n = 3  # starting with a square of side length 3

    while True:
        for _ in range(4):
            if is_prime(n*n - _*(n-1)):
                primes += 1
            total += 1
        if primes / total < ratio:
            return n
        n += 2  # going to the next square

print(first_spiral_below_ratio(0.1))
