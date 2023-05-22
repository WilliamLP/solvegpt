from itertools import permutations

# Outer ring must have the largest numbers
outer_ring = [6, 7, 8, 9, 10]
inner_ring = [1, 2, 3, 4, 5]

# Maximum 16-digit string
max_string = ''

# Permute through all possible combinations
for perm in permutations(range(1, 11)):

    # Split into the two rings
    outer, inner = perm[:5], perm[5:]

    # Ensure the outer ring has larger numbers
    if max(outer) <= 5:
        continue

    # Calculate the sums
    sums = [outer[i] + inner[i] + inner[(i + 1) % 5] for i in range(5)]

    # Check that all the sums are the same
    if len(set(sums)) == 1:

        # Find the index of the minimum in the outer ring
        min_index = outer.index(min(outer))

        # Construct the string
        string = ''.join(str(outer[(min_index + i) % 5]) + str(inner[(min_index + i) % 5]) + str(inner[(min_index + i + 1) % 5]) for i in range(5))

        # Check if the string is longer than 16 digits
        if len(string) > 16:
            continue

        # If the string is the same length, check if it's greater
        if len(string) == len(max_string) and int(string) > int(max_string):
            max_string = string

        # If the string is longer, replace the maximum
        elif len(string) > len(max_string):
            max_string = string

print(max_string)
