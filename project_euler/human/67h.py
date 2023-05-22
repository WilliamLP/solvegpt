



n = 100
triangle = []
with open('triangle.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        ns = [int(nstr) for nstr in line.strip().split(' ')]
        triangle.append(ns)

sums = [[0] * n for _ in range(n)]
for i in reversed(range(100)):
    for j in range(i + 1):
        if i == n - 1:
            sums[i][j] = triangle[i][j]
        else:
            sums[i][j] = triangle[i][j] + max(sums[i+1][j], sums[i+1][j+1])
print(sums[0][0])