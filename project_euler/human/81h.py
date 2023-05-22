
cache = {}
def shortest_path(grid ,i, j):
    if i == 0 and j == 0:
        return grid[i][j]
    if (i, j) not in cache:
        shortest = float('inf')
        if i > 0:
            shortest = min(shortest, shortest_path(grid, i - 1, j))
        if j > 0:
            shortest = min(shortest, shortest_path(grid, i, j - 1))
        cache[(i, j)] = shortest + grid[i][j]
    return cache[(i, j)]

grid = []
with open('matrix.txt', 'r') as f:
    for l in f.readlines():
        grid.append([int(ch) for ch in l.split(',')])

print(shortest_path(grid, len(grid) - 1, len(grid) - 1))