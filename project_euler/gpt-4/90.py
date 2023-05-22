from itertools import combinations

# Step 1: Generate distinct combinations of digits (0-9) taken 6 at a time
# considering 6 and 9 to be the same digit (because one can be flipped to form the other)
combos = list(combinations(range(10), 6))
combos = [combo if 9 not in combo else (*combo[:-1], 6) for combo in combos]
# combos = list(set(combos))  # HUMAN COMMENT OUT

# The square numbers less than 100
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]

distinct_arrangements = 0

# Step 2: Iterate over all pairs of combinations
for i in range(len(combos)):
    for j in range(i, len(combos)):
        cube1 = combos[i]
        cube2 = combos[j]

        # Step 3: Check if all square numbers can be formed
        valid = True
        for square in squares:
            tens, ones = divmod(square, 10)
            # HUMAN MOD
            tens, ones = 6 if tens == 9 else tens, 6 if ones == 9 else ones
            if ((tens in cube1 and ones in cube2) or
                    (tens in cube2 and ones in cube1)):
                continue
            else:
                valid = False
                break

        if valid:
            distinct_arrangements += 1

print(distinct_arrangements)
