from queue import PriorityQueue

def calc_shortest_paths(grid):
    dists = {}
    pq = PriorityQueue()
    pq.put((grid[0][0], (0, 0)))

    while not pq.empty():
        dist, coords = pq.get()
        if coords in dists:
            continue
        dists[coords] = dist
        i, j = coords
        if i > 0:  # up
            pq.put((dist + grid[i - 1][j], (i - 1, j)))
        if i < len(grid) - 1:  # down
            pq.put((dist + grid[i + 1][j], (i + 1, j)))
        if j < len(grid) - 1:  # right
            pq.put((dist + grid[i][j + 1], (i, j + 1)))
        if j > 0:  # left
            pq.put((dist + grid[i][j - 1], (i, j - 1)))

    return dists

grid = []
with open('matrix.txt', 'r') as f:
    for l in f.readlines():
        grid.append([int(ch) for ch in l.split(',')])

dists = calc_shortest_paths(grid)
print(dists[(len(grid) - 1, len(grid) - 1)])
