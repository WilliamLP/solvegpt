from euler import *

primes = set(sieve(10000))
for i in range(1000, 10000):
    if not (i in primes):
        continue
    for j in range(2, 5000, 2):
        if i + 2 * j >= 10000:
            break
        if i + j not in primes or i + 2 * j not in primes:
            continue
        strs = [sorted(''.join(str(i))), sorted(''.join(str(i + j))), sorted(''.join(str(i + 2 * j)))]
        if strs[0] != strs[1] or strs[0] != strs[2]:
            continue
        print(f'{i}{i + j}{i + 2 * j}')

