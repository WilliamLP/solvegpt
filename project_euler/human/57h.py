from fractions import Fraction

term = Fraction(1, 1)
result = 0
for i in range(1, 1001):
    term = 1 + 1 / (1 + term)
    if len(str(term.numerator)) > len(str(term.denominator)):
        result += 1
print(result)
