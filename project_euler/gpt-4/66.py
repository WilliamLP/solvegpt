import math

def solve():
    max_x = 0
    max_d = 0
    for D in range(2, 1001):
        limit = int(math.sqrt(D))
        if limit * limit == D:
            continue
        m = 0
        d = 1
        a = limit

        num_m1 = 1
        num = a

        den_m1 = 0
        den = 1

        while num * num - D * den * den != 1:
            m = d * a - m
            d = (D - m * m) // d
            a = (limit + m) // d

            num_m2 = num_m1
            num_m1 = num

            den_m2 = den_m1
            den_m1 = den

            num = a * num_m1 + num_m2
            den = a * den_m1 + den_m2

        if num > max_x:
            max_x = num
            max_d = D

    return max_d

print(solve())
