import math

def sieve_phi(limit):
    phi = list(range(limit+1))
    for i in range(2, limit+1):
        if phi[i] == i:
            for j in range(i, limit+1, i):
                phi[j] = phi[j] // i * (i-1)
    return phi

def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))

def min_ratio(limit):
    phi = sieve_phi(limit)
    min_ratio = float('inf')
    result = -1
    for n in range(2, limit+1):
        if is_perm(n, phi[n]):
            ratio = n / phi[n]
            if ratio < min_ratio:
                min_ratio = ratio
                result = n
    return result

print(min_ratio(10**7))
