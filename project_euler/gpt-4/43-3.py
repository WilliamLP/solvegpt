import itertools

def has_substring_divisibility_property(pandigital):
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]
    return all(int(pandigital[i:i + 3]) % divisors[i] == 0 for i in range(len(divisors)))

def sum_pandigital_numbers_with_property():
    total_sum = 0
    pandigital_numbers = []
    for d2d3d4 in itertools.permutations('02468', 3):
        for d4d5d6 in itertools.permutations('059', 2):
            for d5d6d7 in itertools.permutations('0123456789', 3):
                if int(d5d6d7[0] + d4d5d6[1]) % 7 != 0:
                    continue
                for d6d7d8 in itertools.permutations('0123456789', 3):
                    if int(d6d7d8[0] + d5d6d7[2]) % 11 != 0:
                        continue
                    for d7d8d9 in itertools.permutations('0123456789', 3):
                        if int(d7d8d9[0] + d6d7d8[2]) % 13 != 0:
                            continue
                        for d8d9d10 in itertools.permutations('0123456789', 3):
                            if int(d8d9d10[0] + d7d8d9[2]) % 17 != 0:
                                continue
                            pandigital = '0' + ''.join(d2d3d4) + d4d5d6[0] + ''.join(d5d6d7) + d6d7d8[1] + ''.join(d7d8d9) + d8d9d10[2]
                            pandigital_numbers.append(pandigital)
                            if has_substring_divisibility_property(pandigital):
                                total_sum += int(pandigital)

    return total_sum, pandigital_numbers

result, pandigital_numbers = sum_pandigital_numbers_with_property()
print(f"Total sum: {result}")
print(f"Pandigital numbers with property: {pandigital_numbers}")
