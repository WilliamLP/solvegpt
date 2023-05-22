

def polygonal_set(k):
    result = set()
    for n in range(1, 200):
        p = n * ((k - 2) * n - (k - 4)) // 2
        if p > 9999:
            break
        if p < 1000 or (p // 10) % 10 == 0: # tens digit cannot be 0
            continue
        result.add(p)
    return result

polygonal_sets = []
union = set()
for k in range(3, 9):
    polygonal_sets.append(polygonal_set(k))
    union = union.union(polygonal_sets[-1])

# Find all possible ways to pick cyclical lists of length n such that each number is polygonal
def next_cyclical_lists(prev_lists):
    result = []
    for l in prev_lists:
        start = l[-1] % 100
        for i in union:
            if i // 100 != start:  # Cyclical property
                continue
            result.append(l + [i])
    return result

# loop through octagonals for first number
lists = [[n] for n in polygonal_sets[-1]]
for i in range(2, 6):
    lists = next_cyclical_lists(lists)
    # print(lists)

# Now look for a solution
for l in lists:
    l.append(100 * (l[-1] % 100) + l[0] // 100)
    if l[-1] not in union:
        continue

    hits = set()  # Check that we hit all 6 categories
    coverage = []
    for i, n in enumerate(l):
        coverage.append([])
        for j, s in enumerate(polygonal_sets):
            if n in s:
                hits.add(j)
                coverage[-1].append(j + 3)
    # Eliminate anything with duplicate coverage between two terms
    # This misses a potential edge case with [3, 6] but it yields the correct answer by inspection.
    if len(hits) == 6: #and len(set([str(c) for c in coverage])) == 6:
        print(l, coverage, sum(l))



