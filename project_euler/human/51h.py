from euler import *

primes = sieve(1000000)
primes_set = set(primes)

def power_set(n):
    result = []
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (2 ** j):
                subset.append(j)
        result.append(subset)
    return result

def solve():
    for p in primes:
        for p_set in power_set(len(str(p))):
            if not p_set:
                continue
            digit_set = set([str(p)[i] for i in p_set])
            if len(digit_set) != 1:
                # Only check digit sets when digits are all the same
                continue
            prime_count = 0
            p_list = list(str(p))
            for d in range(10):  # Substitute digits in the subset
                for pos in p_set:
                    p_list[pos] = str(d)
                if p_list[0] == '0':
                    continue
                if int(''.join(p_list)) in primes_set:
                    prime_count += 1
            if prime_count >= 8:
                print(p)
                return
solve()