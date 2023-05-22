import math

def is_int(n):
    return int(n) == n

M = 0
count = 0

while count <= 1000000:
    M += 1
    if M % 100 == 0:
        print(M)
    for a in range(1, M+1):
        for b in range(a, M+1):
            c = math.sqrt(M*M + (a+b)*(a+b))
            if is_int(c):
                count += 1

print(M)
