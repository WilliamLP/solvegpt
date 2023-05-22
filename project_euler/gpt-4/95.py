def divisorsum(n):
    sum = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n // p
            sum = sum + j
            while n % p == 0:
                n = n // p
                sum = sum + j
                j = j * p
        if p == 2:
            p = 3
        else:
            p = p + 2
    if n > 1:
        sum += n + 1
    return sum

print(divisorsum(999))
LIMIT = 10**3
sumdivs = [0] * (LIMIT + 1)
for i in range(1, LIMIT):
    sumdivs[i] = divisorsum(i) - i

longest = [0, 0]
for i in range(LIMIT, 0, -1):
    visited = []
    j = i
    while sumdivs[j] < LIMIT and j not in visited:
        visited.append(j)
        j = sumdivs[j]
    if j == i:
        if len(visited) > longest[0]:
            longest = [len(visited), i]
        elif len(visited) == longest[0] and i < longest[1]:
            longest[1] = i
print(longest[1])
