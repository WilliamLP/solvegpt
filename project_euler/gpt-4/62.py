from collections import defaultdict

def compute_cube_permutations(n):
    # Create a default dictionary to hold the cubes
    cube_dict = defaultdict(list)
    i = 0
    while True:
        # Calculate the cube of i
        cube = i**3
        # Create a key by sorting the digits of the cube
        key = ''.join(sorted(str(cube)))
        # Add the cube to the list of cubes for this key
        cube_dict[key].append(cube)
        # If we have found n cubes for this key, return the smallest one
        if len(cube_dict[key]) == n:
            return min(cube_dict[key])
        i += 1

# Test the function
print(compute_cube_permutations(5))
