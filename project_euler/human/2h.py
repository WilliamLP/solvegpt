fib0, fib1 = 0, 1
sum = 0
while fib1 <= 4000000:
    if fib1 % 2 == 0:
        sum += fib1
    fib0, fib1 = fib1, fib0 + fib1
print('The sum is: ', sum)