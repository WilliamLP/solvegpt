import math

# Create a list with factorial values for digits
factorials = [math.factorial(i) for i in range(10)]

# Create a cache for memoization
cache = [0] * 3000000

# We know from the problem statement that these lengths are 60
cache[169] = cache[363601] = cache[1454] = cache[871] = cache[45361] = cache[872] = cache[45362] = 60

def sum_factorial_digits(n):
    return sum(factorials[int(digit)] for digit in str(n))

def chain_length(n):
    if n < 3000000 and cache[n] != 0:
        return cache[n]
    else:
        length = 1 + chain_length(sum_factorial_digits(n))
        if n < 3000000:
            cache[n] = length
        return length

count = 0
for i in range(1, 1000000):
    if chain_length(i) == 60:
        count += 1

print(count)
