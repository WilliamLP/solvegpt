import itertools

# Function to check if a ring is magic
def is_magic(ring):
    s = sum(ring[0])
    return all(sum(ring[i]) == s for i in range(1, 5))

# Function to convert a ring to a string
def ring_to_string(ring):
    return ''.join(str(x) for r in ring for x in r)

# The maximum string
max_string = ''

# Iterate over all permutations of 1 to 10
for perm in itertools.permutations(range(1, 11)):
    # Construct the ring
    ring = [perm[i:i+3] for i in range(0, 15, 3)]
    ring.append([perm[0], perm[5], perm[14]])
    # Make sure the lowest number is on the outer ring
    if min(perm[0], perm[3], perm[6], perm[9], perm[12]) != perm[0]:
        continue
    # Check if the ring is magic
    if is_magic(ring):
        # Convert the ring to a string
        s = ring_to_string(ring)
        # Track the maximum string
        if len(s) == 16 and s > max_string:
            max_string = s

print(max_string)
