from queue import PriorityQueue

def calc_shortest_paths(grid):
    dists = {}
    pq = PriorityQueue()
    # Shortest path on left column is the cell weight
    for i in range(len(grid)):
        dists[(i, 0)] = grid[i][0]
        pq.put((grid[i][1] + grid[i][0], (i, 1)))

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

    return dists

grid = []
with open('matrix.txt', 'r') as f:
    for l in f.readlines():
        grid.append([int(ch) for ch in l.split(',')])

dists = calc_shortest_paths(grid)
print(min([dists[(i, len(grid) - 1)] for i in range(len(grid))]))
