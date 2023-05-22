from itertools import permutations
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_largest_pandigital_prime():
    for n in range(7, 0, -1):
        pandigital_numbers = permutations(range(1, n + 1))
        for pandigital in sorted(pandigital_numbers, reverse=True):
            pandigital_number = int("".join(map(str, pandigital)))
            if is_prime(pandigital_number):
                return pandigital_number

largest_pandigital_prime = find_largest_pandigital_prime()
print(largest_pandigital_prime)
