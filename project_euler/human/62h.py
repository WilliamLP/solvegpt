


from collections import defaultdict
i = 1
digits_counts = defaultdict(int)
smallest_cubes = {}
while True:
    cube = i * i * i
    digits = ''.join(sorted(str(cube)))
    if digits not in smallest_cubes:
        smallest_cubes[digits] = cube
    digits_counts[digits] += 1
    if digits_counts[digits] == 5:
        print(smallest_cubes[digits])
        break
    i += 1