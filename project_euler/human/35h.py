from euler import *

primes = set(sieve(1000000))

count_circular = 0
for pr in primes:
    prime_string = str(pr)
    is_circular = True
    for j in range(1, len(prime_string)):
        new_string = prime_string[j:] + prime_string[0:j]
        if int(new_string) not in primes:
            is_circular = False
            break
    if is_circular:
        count_circular += 1
print(count_circular)