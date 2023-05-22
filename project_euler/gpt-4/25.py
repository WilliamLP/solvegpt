def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def find_first_fibonacci_with_n_digits(n):
    for index, fib in enumerate(fibonacci(), start=1):
        if len(str(fib)) >= n:
            return index

n_digits = 1000
result = find_first_fibonacci_with_n_digits(n_digits)
print(result)
