max_p, max_combos = 0, 0
num_combos = {i: 0 for i in range(1, 1001)}
for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = (a * a + b * b) ** 0.5
        if c != int(c) or a + b + c > 1000:
            continue
        p = a + b + int(c)
        num_combos[p] += 1
        if num_combos[p] > max_combos:
            max_p, max_combos = p, num_combos[p]
print(max_p)