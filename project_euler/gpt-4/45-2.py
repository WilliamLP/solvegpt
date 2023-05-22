def pentagonal(n):
    return n * (3*n - 1) // 2

def hexagonal(n):
    return n * (2*n - 1)

def is_pentagonal(num):
    # Inverse of the pentagonal formula
    n = (1 + (1 + 24*num) ** 0.5) / 6
    return n == int(n)

n = 144
while True:
    h = hexagonal(n)
    if is_pentagonal(h):
        print(h)
        break
    n += 1
