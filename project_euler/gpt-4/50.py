def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i, is_prime in enumerate(sieve):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                sieve[n] = False


def longest_sum(limit):
    primes = list(sieve_of_eratosthenes(limit))
    prime_set = set(primes)

    max_length = 0
    max_prime = 0

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            seq_sum = sum(primes[i:j])
            if seq_sum >= limit:
                break

            if seq_sum in prime_set and j - i > max_length:
                max_length = j - i
                max_prime = seq_sum

    return max_prime, max_length


limit = 10**6
prime, length = longest_sum(limit)
print(f"The prime below one-million that can be written as the sum of the most consecutive primes is {prime}, with {length} terms.")
