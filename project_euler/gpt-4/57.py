from fractions import Fraction

def continued_fraction_expansions(n):
    cf = Fraction(1, 2)
    count = 0

    for _ in range(n):
        cf = 1 / (2 + cf)
        expansion = 1 + cf

        if len(str(expansion.numerator)) > len(str(expansion.denominator)):
            count += 1

    return count

print(continued_fraction_expansions(1000))
