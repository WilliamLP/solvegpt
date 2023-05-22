def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_twice_squares(n):
    i = 1
    while True:
        twice_square = 2 * (i ** 2)
        if twice_square > n:
            break
        yield twice_square
        i += 1

def is_goldbach_false():
    primes = set()
    n = 9  # start from the first odd composite number

    while True:
        if is_prime(n):
            primes.add(n)
        else:  # if n is not prime, it must be composite
            if not any(n - p in generate_twice_squares(n) for p in primes):
                return n  # n cannot be written as the sum of a prime and twice a square
        n += 2  # increment by 2 to get the next odd number

print(is_goldbach_false())
