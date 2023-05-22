from fractions import Fraction

largest_fraction = 0
for d in range(2, 1000000):
    if d % 7 == 0:
        continue
    n = 3 * d // 7
    largest_fraction = max(largest_fraction, Fraction(n, d))
print(largest_fraction)