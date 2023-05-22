from euler import *

LIMIT = 1000000
primes = sieve(LIMIT)

cyc_lens = [0] + [None] * (LIMIT)
for n in range(1, LIMIT + 1):
    if cyc_lens[n] is not None:
        continue
    n2 = n
    visited = []
    while True:
        visited.append(n2)
        n2 = sum(proper_divisors(primes, n2))
        if n2 > LIMIT or cyc_lens[n2] is not None:
            # Entered a previous cycle or overflow
            for m in visited:
                cyc_lens[m] = 0
            break
        if n2 in visited:  # Loop!
            i2 = visited.index(n2)
            cyc_len = len(visited) - i2
            for m in visited[:i2]:
                cyc_lens[m] = 0
            for m in visited[i2:]:
                cyc_lens[m] = cyc_len
            break

best_n, best_len = 0, 0
for n, cyc_len in enumerate(cyc_lens):
    if cyc_len > best_len:
        best_n, best_len = n, cyc_len
print(best_n, best_len)