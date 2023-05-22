import math

# Pre-calculate factorials for digits 0-9
factorials = [math.factorial(i) for i in range(10)]

# Chains length cache
chain_length_cache = {169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2, 1: 1, 2: 1, 40585: 1}

def sum_factorial_digits(n):
    return sum(factorials[int(d)] for d in str(n))

def get_chain_length(n):
    chain = []
    while n not in chain:
        if n in chain_length_cache:
            idx = chain.index(n) if n in chain else -1
            length = len(chain) - idx
            for i, link in enumerate(chain):
                if link < 1000000:
                    chain_length_cache[link] = length + max(0, idx - i)
            return chain_length_cache[n]
        chain.append(n)
        n = sum_factorial_digits(n)

# Count chains with 60 non-repeating terms
count = sum(get_chain_length(i) == 60 for i in range(1, 1000000))
print(count)
