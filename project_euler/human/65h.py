from fractions import Fraction
def continued_fraction_val(k):
    if k == 0:
        return 2
    if k % 3 == 2:
        return (k + 1) // 3 * 2
    return 1

def convergent(n):
    vals = [continued_fraction_val(k) for k in range(n)]
    f = Fraction(vals[-1])
    for val in reversed(vals[:-1]):
        f = val + 1 / f
    return f

digits = convergent(100).numerator
print(sum([int(d) for d in str(digits)]))
