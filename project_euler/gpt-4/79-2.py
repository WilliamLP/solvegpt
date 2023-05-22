from collections import defaultdict
import heapq

def read_login_attempts(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

def build_graph(sequences):
    # Create a dictionary where keys are all unique digits in the sequences
    # The values are initially empty lists
    graph = {digit: [] for seq in sequences for digit in seq}

    # Add edges to the graph
    for seq in sequences:
        for i in range(len(seq) - 1):
            # Avoid adding duplicate edges
            if seq[i+1] not in graph[seq[i]]:
                graph[seq[i]].append(seq[i+1])

    return graph

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            in_degree[neighbour] += 1

    heap = [node for node in in_degree if in_degree[node] == 0]
    heapq.heapify(heap)

    result = []
    while heap:
        node = heapq.heappop(heap)
        result.append(node)

        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                heapq.heappush(heap, neighbour)

    return "".join(result)

login_attempts = read_login_attempts('keylog.txt')
graph = build_graph(login_attempts)
passcode = topological_sort(graph)
print(f"The shortest possible secret passcode is {passcode}.")
