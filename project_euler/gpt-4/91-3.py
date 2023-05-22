def num_right_triangles(n):
    # Importing the required function
    from math import gcd

    # Count of triangles with right angle at the origin
    origin_count = 2 * (n * n)

    # Count of triangles with right angle at P (or Q)
    pq_count = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            # Count triangles where P=(x,y) and Q lies on the same horizontal or vertical line as P
            pq_count += 2*(n - 1) # exclude the origin
            # Count triangles where P=(x,y) and Q lies on the line perpendicular to OP at P
            gcd_val = gcd(x, y)
            pq_count += 2*((min(y*gcd_val//x, (n-x+1)*gcd_val//y) - 1) + (min(x*gcd_val//y, (n-y+1)*gcd_val//x) - 1))

    total = origin_count + 4*pq_count  # multiply by 4 for symmetry in other quadrants

    return total


import math
print(num_right_triangles(50))
