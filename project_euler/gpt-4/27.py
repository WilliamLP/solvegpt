def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_coefficients_product(limit_a, limit_b):
    max_primes = 0
    product = 0

    for a in range(-limit_a + 1, limit_a):
        for b in range(-limit_b, limit_b + 1):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1

            if n > max_primes:
                max_primes = n
                product = a * b

    return product

limit_a = 1000
limit_b = 1000
result = find_coefficients_product(limit_a, limit_b)
print(result)
