def divisorsum(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i == (n / i):
                sum = sum + i
            else:
                sum = sum + (i + n//i)
    return sum

LIMIT = 10**6
sumdivs = [0] * (LIMIT + 1)
for i in range(1, LIMIT):
    sumdivs[i] = divisorsum(i)

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
