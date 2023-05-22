def fibonacci(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a + b

def even_sum(limit):
    even_fibonacci = (fib for fib in fibonacci(limit) if fib % 2 == 0)
    return sum(even_fibonacci)

result = even_sum(4000000)
print(result)
