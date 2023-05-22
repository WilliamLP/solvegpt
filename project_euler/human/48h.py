
sum_mod = 0
for i in range(1, 1001):
    sum_mod = (sum_mod + i ** i) % 10 ** 10
print(sum_mod)