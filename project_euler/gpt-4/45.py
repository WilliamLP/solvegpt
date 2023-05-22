def triangle_numbers(n):
    return n * (n + 1) // 2

def pentagonal_numbers(n):
    return n * (3*n - 1) // 2

def hexagonal_numbers(n):
    return n * (2*n - 1)

n = 286
while True:
    t = triangle_numbers(n)
    i, p = 166, 0
    while p < t:
        p = pentagonal_numbers(i)
        i += 1
    if p == t:
        j, h = 144, 0
        while h < t:
            h = hexagonal_numbers(j)
            j += 1
        if h == t:
            print(t)
            break
    n += 1
