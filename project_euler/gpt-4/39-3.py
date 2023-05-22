from math import gcd

def count_right_triangles(p_limit):
    counts = {}

    for m in range(2, int((p_limit // 2)**0.5) + 1):
        for n in range(1, m):
            p = 2 * m * (m + n)
            if p > p_limit:
                break
            if gcd(m, n) == 1:
                counts[p] = counts.get(p, 0) + 1

    return counts

p_limit = 1000
triangle_counts = count_right_triangles(p_limit)
max_p = max(triangle_counts, key=triangle_counts.get)

print(max_p)
