from euler import *
primes = sieve(9999)

sum = 0
for n in range(1000, 10000):
    divs = proper_divisors(primes, n)
    for div in divs:
        if div * div > n:
            continue
        div2 = n // div
        digits_str = str(n) + str(div) + str(div2)
        if len(digits_str) != 9 or '0' in digits_str:
            continue
        digits_set = set([ch for ch in digits_str])
        if len(digits_set) == 9:
            print(f'{div} * {div2} = {n}')
            sum += n
            break
print(sum)