def divisible_by_all(n):
    for j in range(1, 21):
        if n % j != 0:
            return False
    return True

i = 19
while not divisible_by_all(i):
    i += 19
print(i)