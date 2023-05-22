# Number of form x0 = (sqrt(n) + b) / (c)
# Returns: a and representation of x1, such that x0 = a + 1/x1
def next_term(n, b, c):
    a = int((n**0.5 + b) / c)
    # x0 = a + (sqrt(n) + b - a*c) / c
    # x1 = c / (sqrt(n) + b - a*c)
    # (complete the square)
    # x1 = c * (sqrt(n) - b + a*c) / (n - b*b + 2*b*a*c - a*a*c*c)
    # x1 = (sqrt(n) - b + a*c) / ((n - b*b)/c + 2*b*a - a*a*c
    # Why is n - b*b divisible by c?
    b_1, c_1 = a*c - b, (n - b*b) // c + 2*a*b - a*a*c
    return a, b_1, c_1
    # Note n - b_1*b_1 = n - a*a*c*c + 2*a*b*c - b*b
    # = c-1 * c
    # So, by recursion n - b*b is still divisible by c


def continued_fraction_period(n):
    if int(n ** 0.5) ** 2 == n:
        return 0
    a, b, c = next_term(n, 0, 1)
    i = 0
    i_lookup = {(b, c): 0}
    while True:  #  Detect cycle
        i += 1
        a, b, c = next_term(n, b, c)
        if (b, c) in i_lookup:
            return i - i_lookup[(b, c)]
        i_lookup[(b, c)] = i

periods = [continued_fraction_period(n) for n in range(1, 1001)]
count = len([p for p in periods if p % 2 == 1])
for i, p in enumerate(periods):
    print(i, p)