def polygonal(s, n):
    if s == 3: # Triangle
        return n * (n + 1) // 2
    elif s == 4: # Square
        return n * n
    elif s == 5: # Pentagonal
        return n * (3 * n - 1) // 2
    elif s == 6: # Hexagonal
        return n * (2 * n - 1)
    elif s == 7: # Heptagonal
        return n * (5 * n - 3) // 2
    elif s == 8: # Octagonal
        return n * (3 * n - 2)

polygonals = {}
for s in range(3, 9):
    polygonals[s] = []
    n = 1
    while True:
        p = polygonal(s, n)
        if p < 1000:
            n += 1
        elif p < 10000:
            polygonals[s].append(p)
            n += 1
        else:
            break

def find_cyclic_set(numbers, polygonal_types, current_set):
    if len(current_set) == 6 and current_set[0] // 100 == current_set[-1] % 100:
        return current_set
    for s in polygonal_types:
        for number in numbers[s]:
            if len(current_set) == 0 or current_set[-1] % 100 == number // 100:
                new_polygonal_types = polygonal_types.copy()
                new_polygonal_types.remove(s)
                new_set = current_set + [number]
                result = find_cyclic_set(numbers, new_polygonal_types, new_set)
                if result is not None:
                    return result
    return None

cyclic_set = find_cyclic_set(polygonals, list(range(3, 9)), [])
print(sum(cyclic_set))
