import heapq

def read_matrix():
    with open('matrix.txt', 'r') as f:
        matrix = [[int(num) for num in line.split(',')] for line in f]
    return matrix

def min_path(matrix):
    heap = [(matrix[0][i], 0, i) for i in range(len(matrix[0]))]
    heapq.heapify(heap)
    seen = set()

    while heap:
        (cost, x, y) = heapq.heappop(heap)
        if (x, y) in seen:
            continue
        seen.add((x, y))

        if x == len(matrix) - 1:
            return cost

        # up
        if y > 0 and (x, y - 1) not in seen:
            heapq.heappush(heap, (cost + matrix[y - 1][x], x, y - 1))

        # down
        if y < len(matrix) - 1 and (x, y + 1) not in seen:
            heapq.heappush(heap, (cost + matrix[y + 1][x], x, y + 1))

        # right
        if x < len(matrix[0]) - 1 and (x + 1, y) not in seen:
            heapq.heappush(heap, (cost + matrix[y][x + 1], x + 1, y))

matrix = read_matrix()
print(min_path(matrix))
