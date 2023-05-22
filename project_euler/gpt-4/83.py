import heapq

def read_matrix(filename):
    with open(filename, 'r') as f:
        matrix = [[int(num) for num in line.split(',')] for line in f]
    return matrix

def shortest_path(matrix):
    n = len(matrix)
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = matrix[0][0]
    heap = [(matrix[0][0], 0, 0)]
    while heap:
        curr_dist, i, j = heapq.heappop(heap)
        if curr_dist == dist[i][j]:
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    new_dist = curr_dist + matrix[ni][nj]
                    if new_dist < dist[ni][nj]:
                        dist[ni][nj] = new_dist
                        heapq.heappush(heap, (new_dist, ni, nj))
    return dist[-1][-1]

def main():
    matrix = read_matrix('matrix.txt')
    print(shortest_path(matrix))

if __name__ == "__main__":
    main()
