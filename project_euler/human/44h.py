pents = []
for i in range(1, 100000):
    pents.append(i * (3 * i - 1) // 2)
print('Increment d:', pents[-1] - pents[-2])
pents_set = set(pents)

best_d = 99999999
for i, p1 in enumerate(pents):
    for p2 in pents[i+1:]:
        if p2 - p1 not in pents_set or p2 + p1 not in pents_set:
            continue
        best_d = min(best_d, p2 - p1)
print(best_d)