def farey_left(n, d, limit):
    a, b, c, r = 0, 1, 1, d
    while b <= limit and r > n:
        k = (limit + b) // d
        a, b, c, r = c, r, k*c - a, k*r - b
    return a

print(farey_left(3, 7, 10**6))
