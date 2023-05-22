import itertools
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

def next_diagonal():
    """Generate numbers on the diagonals of the spiral."""
    yield 1
    for layer in itertools.count(1):
        start = layer * layer * 4 - layer * 2 + 1
        step = layer * 2
        for _ in range(4):
            yield start
            start += step

def first_spiral_below_ratio(ratio):
    """Find the side length of the spiral where the ratio of primes on the diagonals first falls below a given ratio."""
    primes = 0
    total = 1  # corrected here
    for n, diagonal in enumerate(next_diagonal(), 1):
        if is_prime(diagonal):
            primes += 1
        total += 1
        if n > 1 and primes / total < ratio:
            return n // 2 + 1

print(first_spiral_below_ratio(0.1))
