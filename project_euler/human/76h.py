from collections import defaultdict
partition_counts = defaultdict(int)
def partition_count(n, max_pick):
    if max_pick == 1 or n == 0:
        return 1
    if (n, max_pick) not in partition_counts:
        partition_counts[(n, max_pick)] = partition_count(n - max_pick, min(max_pick, n - max_pick)) +\
            partition_count(n, max_pick - 1)
    return partition_counts[(n, max_pick)]

print(partition_count(100, 99))