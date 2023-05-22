from euler import *

sum = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for prt in permutations(10):
    prt_string = ''.join([str(dgt) for dgt in prt])

    divisible_all = True
    for i, prime in enumerate(primes):
        sub_number = int(prt_string[i + 1:i + 4])
        if sub_number % prime != 0:
            divisible_all = False
            break
    if divisible_all:
        sum += int(prt_string)
print(sum)