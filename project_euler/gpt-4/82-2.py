import numpy as np

# Load the matrix
matrix = np.loadtxt('matrix.txt', delimiter=',')

# Get the size of the matrix
n = matrix.shape[0]

# Initialize a matrix to hold the minimum path sums
min_path_sums = np.zeros((n, n))
min_path_sums[:, 0] = matrix[:, 0]

for i in range(1, n):
    # Update the minimum path sum for the cell directly to the right
    min_path_sums[:, i] = min_path_sums[:, i - 1] + matrix[:, i]

    # For each cell in the column, consider paths through the cell above
    for j in range(1, n):
        min_path_sums[j, i] = min(min_path_sums[j, i], min_path_sums[j - 1, i] + matrix[j, i])

    # For each cell in the column, consider paths through the cell below
    for j in range(n - 2, -1, -1):
        min_path_sums[j, i] = min(min_path_sums[j, i], min_path_sums[j + 1, i] + matrix[j, i])

print(min(min_path_sums[:, -1]))
