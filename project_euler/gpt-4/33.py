from fractions import Fraction

def is_curious_fraction(numerator, denominator):
    common_digit = set(str(numerator)) & set(str(denominator))
    if len(common_digit) != 1 or '0' in common_digit:
        return False

    common_digit = int(list(common_digit)[0])
    remaining_numerator = int(str(numerator).replace(str(common_digit), '', 1))
    remaining_denominator = int(str(denominator).replace(str(common_digit), '', 1))

    if remaining_denominator == 0:
        return False

    return Fraction(numerator, denominator) == Fraction(remaining_numerator, remaining_denominator)

curious_fractions = []

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if is_curious_fraction(numerator, denominator):
            curious_fractions.append(Fraction(numerator, denominator))

product = Fraction(1, 1)
for fraction in curious_fractions:
    product *= fraction

result = product.denominator
print(result)
