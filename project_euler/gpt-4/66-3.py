import math

def solve_pells_equation(limit):
    max_x, max_d = 0, 0

    for D in range(2, limit + 1):
        r = math.sqrt(D)
        if r.is_integer():
            continue

        # compute the continued fraction
        m, d, a = 0, 1, int(r)
        conv = [(a, 1)]
        while a != 2 * conv[0][0]:
            m = d * a - m
            d = (D - m * m) // d
            a = int((conv[0][0] + m) / d)
            conv.append((a, 1))

        # compute the convergents and find the solution
        for i in range(1, len(conv)):
            conv[i] = (conv[i-1][0]*conv[i][0] + conv[i][1], conv[i][0])
            x, y = conv[i]
            if x * x - D * y * y == 1:
                if x > max_x:
                    max_x, max_d = x, D
                break

    return max_d

print(solve_pells_equation(1000))
