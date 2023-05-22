from itertools import combinations

# Step 1: Generate distinct combinations of digits (0-9) taken 6 at a time
combos = list(combinations(range(10), 6))

distinct_arrangements = 0
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Step 2: Iterate over all pairs of combinations
for i in range(len(combos)):
    for j in range(i, len(combos)):
        cube1 = set(combos[i])
        cube2 = set(combos[j])

        # Replace 9 with 6 in the cubes as it can be flipped
        cube1 = cube1 if 9 not in cube1 else (cube1 - {9}) | {6}
        cube2 = cube2 if 9 not in cube2 else (cube2 - {9}) | {6}

        # Step 3: Check if all square numbers can be formed
        valid = True
        for square in squares:
            tens, ones = divmod(square, 10)
            if ((tens in cube1 and ones in cube2) or
                    (tens in cube2 and ones in cube1)):
                continue
            else:
                valid = False
                break

        if valid:
            distinct_arrangements += 1

print(distinct_arrangements)
