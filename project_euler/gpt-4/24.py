import math

def find_millionth_permutation(digits, target_permutation):
    permutation = []
    remaining_digits = digits[:]
    factorial_base = len(digits) - 1
    current_target = target_permutation - 1

    for i in range(factorial_base, -1, -1):
        factorial = math.factorial(i)
        index = current_target // factorial
        current_target %= factorial
        permutation.append(remaining_digits.pop(index))

    return ''.join(str(digit) for digit in permutation)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target_permutation = 1000000
millionth_permutation = find_millionth_permutation(digits, target_permutation)

print("The millionth lexicographic permutation of the digits 0-9 is:", millionth_permutation)
