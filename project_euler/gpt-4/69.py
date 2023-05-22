def max_n_over_phi(limit):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = 1
    i = 0
    while result * primes[i] <= limit:
        result *= primes[i]
        i += 1
    return result

print(max_n_over_phi(1000000))
