from math import gcd

def count_right_triangles(p):
    count = 0
    for m in range(2, int((p // 2)**0.5) + 1):
        for n in range(1, m):
            if (2 * m * (m + n)) == p and gcd(m, n) == 1:
                count += 1
    return count

max_solutions = 0
max_p = 0

for p in range(1, 1001):
    solutions = count_right_triangles(p)
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p

print(max_p)
