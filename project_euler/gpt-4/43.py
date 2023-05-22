import itertools

def has_substring_divisibility_property(num_str):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i, divisor in enumerate(divisors, start=1):
        if int(num_str[i:i + 3]) % divisor != 0:
            return False
    return True

def sum_pandigital_numbers_with_property():
    total_sum = 0
    for perm in itertools.permutations('0123456789'):
        num_str = ''.join(perm)
        if has_substring_divisibility_property(num_str):
            total_sum += int(num_str)
    return total_sum

result = sum_pandigital_numbers_with_property()
print(result)
