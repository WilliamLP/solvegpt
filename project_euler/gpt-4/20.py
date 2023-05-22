def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_digits(number):
    return sum(map(int, str(number)))

number = 100
factorial_100 = factorial(number)
sum_digits = sum_of_digits(factorial_100)
print(sum_digits)

