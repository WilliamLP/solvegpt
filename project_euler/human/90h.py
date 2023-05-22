from itertools import combinations

def digit_on_die(d, die):
    return d in die or d == 6 and 9 in die or d == 9 and 6 in die

sq1 = [i*i // 10 for i in range(10)]
sq2 = [i*i % 10 for i in range(10)]
count = 0
for d1 in combinations(range(10), 6):
    for d2 in combinations(range(10), 6):
        if d2 < d1:
            continue
        if d1 == (0, 5, 6, 7, 8, 9) and d2 == (1, 2, 3, 4, 8, 9):
            print('break')
        valid = True
        for i in range(1, 10):  # Test both combinations of dice
            if not (digit_on_die(sq1[i], d1) and digit_on_die(sq2[i], d2)) \
                    and not (digit_on_die(sq1[i], d2) and digit_on_die(sq2[i], d1)):
                valid = False
        if valid:
            count += 1
            continue
        valid = True  # Test the other arrangement
print(count)
