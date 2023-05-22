
count = 0
n = 1
while n <= 22:
    k = 1
    while True:
        d = len(str(k ** n))
        if d == n:
            count += 1
        if d > n:
            break
        k += 1
    n += 1
print(count)