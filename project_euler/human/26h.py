max_k = 0
d_with_max_k = 0
for d in range(1, 1000):
    d2 = d
    while d2 % 2 == 0:
        d2 //= 2
    while d2 % 5 == 0:
        d2 //= 5
    k = 1
    while (10 ** k - 1) % d2 != 0:
        k += 1
    if k > max_k:
        max_k, d_with_max_k = k, d

print(d_with_max_k)