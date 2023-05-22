

from itertools import combinations, product, permutations

def operate(a, b, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b if b != 0 else float('inf')

best_d_set, best_score = None, 0
for d_set in combinations(range(1, 10), 4):
    found = set()
    for ord_ds in permutations(d_set):
        for operators in product('+-/*', repeat=3):
            for first_op in range(3):
                d_set3 = ord_ds[:first_op] +\
                         (operate(ord_ds[first_op], ord_ds[first_op+1], operators[0]),) +\
                         ord_ds[first_op+2:]
                for second_op in range(2):
                    d_set2 = d_set3[:second_op] + \
                             (operate(d_set3[second_op], d_set3[second_op+1], operators[1]),) +\
                             d_set3[second_op+2:]
                    final = operate(d_set2[0], d_set2[1], operators[2])
                    if final == float('inf') or int(final) - final != 0 or final <= 0:
                        continue
                    found.add(int(final))

    for i in range(1, len(found)):
        if i not in found:
            if i - 1 > best_score:
                best_d_set, best_score = d_set, i - 1
                print(best_d_set, best_score)
            break
