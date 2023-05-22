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


for k in range(1, 1000000):  # arbitrarily large limit
    f = convergent(2, k)  # Approximate square root of 2
    test = f.numerator ** 2 - 2 * f.denominator ** 2
    if test == -1 and f.numerator % 2 == 1 and f.denominator % 2 == 1:
        b, t = (f.denominator + 1) // 2, (f.numerator + 1) // 2
        print(b, t)
        if t > 10 ** 12:
            break

