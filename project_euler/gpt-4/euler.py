from collections import defaultdict

def sieve(n):
    primes = [2, 3]
    composites = [False] * (n + 1)
    t = 5
    while(t <= n):
        for i in [t, t + 2]:
            if i <= n and not composites[i]:
                primes.append(i)
                j = i + i
                while j < n:
                    composites[j] = True
                    j += i
        t += 6
    return primes

def prime_factors(primes, n):
    # Factors n and returns a dictionary of {prime factor : multiplicity}
    result = defaultdict(int)
    for pr in primes:
        if pr * pr > n:
            break
        while pr < n and n % pr == 0:
            result[pr] += 1
            n //= pr
    # Than n left must be prime
    result[n] += 1
    return result

def least_prime_factor(primes, n):
    for pr in primes:
        if n % pr == 0:
            return pr

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

def _permutations(nums):
    if len(nums) == 1:
        return [[nums[0]]]
    result = []
    for i in range(len(nums)):
        first = [nums[i]]
        rest = [nums[j] for j in range(len(nums)) if j != i]
        result.extend([first + p for p in _permutations(rest)])
    return result

def permutations(n):
    return _permutations([i for i in range(n)])

def is_prime(n):
    if n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def totient(primes, n):
    tot = 1
    pf = prime_factors(primes, n)
    for p, mult in pf.items():
        tot *= (p ** mult - p ** (mult - 1))
    return tot

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n