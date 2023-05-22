from fractions import Fraction

# From a number of form x0 = (sqrt(n) + b) / (c)
# Returns: a and representation of x1, such that x0 = a + 1/x1
def next_sqrt_continued_fraction_term(n, b, c):
    a = int((n**0.5 + b) / c)
    b_1, c_1 = a*c - b, (n - b*b) // c + 2*a*b - a*a*c
    return a, b_1, c_1

# Expands the continued fraction for sqrt(n) to k terms, returns the fraction
def convergent(n, k):
    b, c = 0, 1
    continued_fraction_terms = []
    for i in range(k):
        a, b, c = next_sqrt_continued_fraction_term(n, b, c)
        continued_fraction_terms.append(a)
    f = Fraction(continued_fraction_terms[-1])
    for val in reversed(continued_fraction_terms[:-1]):
        f = val + 1 / f
    return f

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

best_d, best_x = 0, 0
for d in range(2, 1001):
    if is_perfect_square(d):
        continue
    for k in range(1, 1000000):  # arbitrarily large limit
        f = convergent(d, k)
        test = f.numerator ** 2 - d * f.denominator ** 2
        if test == 1:
            if f.numerator > best_x:
                best_d, best_x = d, f.numerator
            break

print(best_d, best_x)