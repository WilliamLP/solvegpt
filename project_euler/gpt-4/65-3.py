from fractions import Fraction

def e_sequence():
    yield 2
    n = 2
    while True:
        yield 1
        yield n
        yield 1
        n += 2

def convergent(seq, n):
    frac = Fraction(next(seq))
    for _ in range(n - 1):
        frac = next(seq) + Fraction(1, frac)
    return frac

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

seq = e_sequence()
frac = convergent(seq, 100)
result = sum_digits(frac.numerator)

print(result)
