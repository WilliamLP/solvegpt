def partition(n):
    # The number of ways can be stored in a 2D list
    ways = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

    # The number of ways to partition n using 1 is always 1
    for i in range(n + 1):
        ways[i][1] = 1

    # Fill the rest of the 2D list
    for i in range(1, n + 1):
        for j in range(2, n + 1):
            if i < j:
                ways[i][j] = ways[i][i]
            elif i == j:
                ways[i][j] = 1 + ways[i][j-1]
            else:
                ways[i][j] = ways[i][j-1] + ways[i-j][j]

    return ways[n][n]

n = 100
print(partition(n) - 1)  # Subtract 1 to exclude the number itself as a partition
