import math

def solve_pells_equation(limit):
    max_x, max_d = 0, 0

    for D in range(2, limit + 1):
        r = math.sqrt(D)
        if r == int(r):
            continue
        a, p, q, k = int(r), int(r), 1, int(2*r)
        x, y, nx, ny = 1, 0, a, 1

        while x*x - D*y*y != 1:
            p, q = k*q - p, (D - p*p) // q
            a = (int(r) + p) // q
            k = int(r + p) // q
            x, y, nx, ny = nx, ny, a*nx + x, a*ny + y

        if x > max_x:
            max_x, max_d = x, D

    return max_d

print(solve_pells_equation(10000))
