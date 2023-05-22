from sympy import primerange, isprime
from itertools import combinations

# Generate primes
primes = list(primerange(0, 10000))

# Create adjacency list
graph = {p: [] for p in primes}

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if isprime(int(str(primes[i]) + str(primes[j]))) and isprime(int(str(primes[j]) + str(primes[i]))):
            graph[primes[i]].append(primes[j])
            graph[primes[j]].append(primes[i])

# Depth-first search for clique of size 5
def find_clique(start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    if len(visited) == 5:
        return visited

    for neighbor in graph[start]:
        if visited.isdisjoint(graph[neighbor]):
            continue

        clique = find_clique(neighbor, visited)
        if clique is not None:
            return clique

    visited.remove(start)

# Find minimum sum of clique of size 5
min_sum = float('inf')
min_clique = None

for prime in primes:
    clique = find_clique(prime)
    if clique is not None:
        clique_sum = sum(clique)
        if clique_sum < min_sum:
            min_sum = clique_sum
            min_clique = clique

print(min_sum, min_clique)
