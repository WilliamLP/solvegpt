def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(num):
    pent_test = (1 + (1 + 24 * num)**0.5) / 6
    return pent_test == int(pent_test)

def find_min_pentagonal_diff():
    n = 1
    while True:
        pn = pentagonal(n)
        for m in range(n - 1, 0, -1):
            pm = pentagonal(m)
            if is_pentagonal(pn + pm) and is_pentagonal(pn - pm):
                return pn - pm
        n += 1

D = find_min_pentagonal_diff()
print("The minimized value of D is:", D)

p, q, p + q, q - p

