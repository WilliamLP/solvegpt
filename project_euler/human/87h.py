from euler import *

LIMIT = 50000000
primes = sieve(10000)

pr_pows = {2: [], 3: [], 4: []}
for pr in primes:
    if pr ** 2 > LIMIT:
        break
    for pw in range(2, 5):
        pr_pow = pr ** pw
        if pr_pow <= LIMIT:
            pr_pows[pw].append(pr_pow)

summable = set()
for p2 in pr_pows[2]:
    for p3 in pr_pows[3]:
        if p2 + p3 > LIMIT:
            break
        for p4 in pr_pows[4]:
            if p2 + p3 + p4 > LIMIT:
                break
            summable.add(p2 + p3 + p4)

print(len(summable))