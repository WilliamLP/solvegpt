from sympy import primerange, isprime
from itertools import combinations

def primes_set(num):
    primes = list(primerange(0, num))
    for comb in combinations(primes, 5):
        if is_valid(comb):
            return sum(comb)
    return None

def is_valid(primes):
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if not (isprime(int(str(primes[i]) + str(primes[j]))) and isprime(int(str(primes[j]) + str(primes[i])))):
                return False
    return True

print(primes_set(10000))  # Adjust the range as needed
