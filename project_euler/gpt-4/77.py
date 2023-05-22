from sympy import primerange

def find_value(ways):
    limit = 2
    while True:
        primes = list(primerange(2, limit+1))
        dp = [0]*(limit+1)
        dp[0] = 1

        for prime in primes:
            for i in range(prime, limit+1):
                dp[i] += dp[i-prime]

        if dp[limit] > ways:
            return limit
        limit += 1

print(find_value(5000))
