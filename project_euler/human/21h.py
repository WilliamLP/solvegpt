from euler import *

def proper_divisors(primes, n):
    result = []
    pf_dict = prime_factors(primes, n)
    pf = list(pf_dict.keys())
    vec = [pf_dict[p] for p in pf]
    product = n
    while True:
        i = 0
        while True:
            if vec[i] > 0:
                vec[i] -= 1
                product //= pf[i]
                break
            else:
                vec[i] = pf_dict[pf[i]]
                product *= pf[i] ** pf_dict[pf[i]]
                i += 1
                if i == len(vec):
                    return result
        result.append(product)


def d(primes, n):
    return sum(proper_divisors(primes, n))

primes = sieve(1000000)
amicable_sum = 0
for i in range(2, 1000000):
    d1 = d(primes, i)
    if d1 != i and d(primes, d1) == i:
        amicable_sum += i
print(amicable_sum)
