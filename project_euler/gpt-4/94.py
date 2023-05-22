import math

def almost_equilateral_triangles(perimeter_limit):
    # Initialize sum of perimeters to zero
    sum_of_perimeters = 0

    # Initialize the "fundamental solution" to the Pell equation
    # (2x+1)^2 - 3y^2 = 1 with (x, y) = (1, 1). This is the solution
    # corresponding to the 5-5-6 triangle.
    x = 1
    y = 1

    while True:
        # Generate the next solution to the Pell equation using the recurrence
        # relation (x_{n+1}, y_{n+1}) = (2x_n + 3y_n, 2y_n + x_n). This gives
        # the sides of the next almost equilateral triangle.
        x, y = 2*x + 3*y, 2*y + x

        # Check the perimeters of the two almost equilateral triangles that can
        # be formed from this solution to the Pell equation: one has sides
        # (2x+1, 2x+1, 2x) and the other has sides (2x+1, 2x+1, 2x+2).
        if 6*x + 2 <= perimeter_limit:
            sum_of_perimeters += 6*x + 2
        else:
            break

        if 6*x + 4 <= perimeter_limit:
            sum_of_perimeters += 6*x + 4

    return sum_of_perimeters

# Call the function with perimeter_limit = 1,000,000,000
print(almost_equilateral_triangles(1_000_000_000))
