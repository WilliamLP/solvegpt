def count_right_triangles(p):
    count = 0
    for a in range(1, p//2):
        for b in range(a, (p - a)//2):
            c = p - a - b
            if a * a + b * b == c * c:
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
