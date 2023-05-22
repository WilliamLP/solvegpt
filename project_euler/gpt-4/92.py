def get_next_number(n):
    total = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total += digit ** 2
    return total

ends_in_89 = {89}
ends_in_1 = {1}
count = 0

for i in range(1, 10000000):
    sequence = [i]
    while sequence[-1] not in ends_in_89 and sequence[-1] not in ends_in_1:
        sequence.append(get_next_number(sequence[-1]))
    if sequence[-1] in ends_in_89:
        count += 1
        ends_in_89.update(sequence)
    else:
        ends_in_1.update(sequence)

print(count)
