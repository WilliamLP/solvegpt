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

        # Step 3: Check if all square numbers can be formed
        valid = True
        for square in squares:
            tens, ones = divmod(square, 10)
            # Add a check for 6 and 9 as they can be flipped
            tens_to_check = {tens} | ({9} if tens == 6 else set()) | ({6} if tens == 9 else set())
            ones_to_check = {ones} | ({9} if ones == 6 else set()) | ({6} if ones == 9 else set())
            if not ((bool(tens_to_check & cube1) and bool(ones_to_check & cube2)) or
                    (bool(tens_to_check & cube2) and bool(ones_to_check & cube1))):
                valid = False
                break

        if valid:
            distinct_arrangements += 1

print(distinct_arrangements)
