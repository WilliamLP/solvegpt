def num_right_triangles(n):
    # Count of triangles with right angle at the origin
    origin_count = n*n*(n*n-1)//2  # Choose any two points from n*n points excluding the origin

    # Count of triangles with right angle at P (or Q)
    pq_count = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            gcd = math.gcd(x, y)
            pq_count += min(y*gcd//x, (n-x+1)*gcd//y) - 1
            pq_count += min(x*gcd//y, (n-y+1)*gcd//x) - 1

    total = origin_count + 2*pq_count  # multiply by 2 for symmetry case

    return total


import math
print(num_right_triangles(50))
