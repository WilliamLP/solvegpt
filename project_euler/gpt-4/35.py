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

def rotations(n):
    str_n = str(n)
    return [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]

def is_circular_prime(n):
    return all(is_prime(rot) for rot in rotations(n))

circular_primes = [n for n in range(2, 1000000) if is_circular_prime(n)]
print(len(circular_primes))
