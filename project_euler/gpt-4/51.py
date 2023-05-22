from itertools import combinations

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_family():
    def family_size(n, indices):
        cnt = 0
        for digit in '0123456789':
            n_list = list(str(n))
            for index in indices:
                n_list[index] = digit
            if n_list[0] != '0':
                if is_prime(int("".join(n_list))):
                    cnt += 1
        return cnt

    n = 11
    while True:
        str_n = str(n)
        last_digit = str_n[-1]
        if last_digit in '1379':
            indices = [i for i in range(len(str_n)-1)]
            for r in range(1, len(indices)+1):
                for combination in combinations(indices, r):
                    if family_size(n, combination) == 8:
                        return n
        n += 2

print(prime_family())
