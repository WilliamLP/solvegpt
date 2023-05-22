import math

def is_int(n):
    return int(n) == n

M = 0
count = 0

while count <= 2000:
    M += 1
    for a in range(1, M+1):
        for b in range(a, M+1):
            c1 = math.sqrt(M*M + (a+b)*(a+b))
            # c2 = math.sqrt(M*M + (b+M)*(b+M))
            # c3 = math.sqrt(M*M + (a+M)*(a+M))
            if is_int(c1): # or is_int(c2) or is_int(c3):
                count += 1

print(M)
