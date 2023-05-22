def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while i < n and n % i == 0:
            n //= i
        i += (1 if i == 2 else 2)
    return n

print('Largest prime factor:', largest_prime_factor(600851475143))