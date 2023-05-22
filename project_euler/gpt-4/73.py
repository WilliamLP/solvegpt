def count_fractions(limit):
    a, b, c, d = 0, 1, 1, limit
    result = 0
    while c/d < 1/2:
        if c/d > 1/3:
            result += 1
        k = (limit + b) // d
        a, b, c, d = c, d, k*c - a, k*d - b
    return result

print(count_fractions(12000))

# 7295373