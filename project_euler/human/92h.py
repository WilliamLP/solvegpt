
cache = {}
def ending_cycle(n):
    if n == 1 or n == 89:
        return n
    if n not in cache:
        next = sum([int(d) ** 2 for d in str(n)])
        cache[n] = ending_cycle(next)
    return cache[n]
print(len([n for n in range(1, 10000000) if ending_cycle(n) == 89]))