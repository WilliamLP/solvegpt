def rectangle_count(m, n):
    return (m*(m+1)/2) * (n*(n+1)/2)

def closest_to_two_million():
    closest_area = 0
    difference = 2 * 10**6  # initialize with a high value
    for m in range(1, 100):  # arbitrary range, increase if needed
        for n in range(1, 100):  # arbitrary range, increase if needed
            count = rectangle_count(m, n)
            if abs(2 * 10**6 - count) < difference:
                difference = abs(2 * 10**6 - count)
                closest_area = m * n
    return closest_area

print(closest_to_two_million())
