
max_pandigital = 0
for i in range(1, 10000):
    test_string = str(i)
    j = 1
    while len(test_string) < 9:
        j += 1
        test_string += str(i * j)
    if ''.join(sorted([ch for ch in test_string])) == '123456789':
        max_pandigital = max(max_pandigital, int(test_string))
print(max_pandigital)