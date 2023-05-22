import math

def is_curious_number(num):
    digit_factorial_sum = sum(math.factorial(int(digit)) for digit in str(num))
    return num == digit_factorial_sum

# Since 9! = 362880, the largest number we need to check is 7 * 9! = 2540160
upper_limit = 7 * math.factorial(9)

curious_numbers = [num for num in range(10, upper_limit) if is_curious_number(num)]
result = sum(curious_numbers)

print("The sum of all numbers equal to the sum of the factorial of their digits is:", result)
