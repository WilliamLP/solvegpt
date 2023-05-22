def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

L = 1500000
count = [0] * (L + 1)
m_limit = int((L/2)**0.5)

for m in range(2, m_limit+1):
    for n in range(1 if m % 2 == 0 else 2, m, 2):
        if gcd(m, n) == 1:
            p = 2*m*(m+n)
            for k in range(p, L+1, p):
                count[k] += 1

print(count.count(1))
