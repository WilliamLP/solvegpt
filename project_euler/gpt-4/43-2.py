def is_divisible(substring, divisor):
    return int(substring) % divisor == 0


def backtrack(partial, remaining_digits, total_sum):
    if not remaining_digits:
        if has_substring_divisibility_property(partial):
            total_sum[0] += int(partial)
        return

    for digit in remaining_digits:
        new_partial = partial + digit
        new_remaining_digits = remaining_digits.replace(digit, '', 1)
        backtrack(new_partial, new_remaining_digits, total_sum)


def has_substring_divisibility_property(num_str):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i, divisor in enumerate(divisors, start=1):
        if not is_divisible(num_str[i:i + 3], divisor):
            return False
    return True


def sum_pandigital_numbers_with_property():
    total_sum = [0]
    backtrack("", "0123456789", total_sum)
    return total_sum[0]


result = sum_pandigital_numbers_with_property()
print(result)
