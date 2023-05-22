chain_lengths = {}
def chain_length(n):
    if n == 1:
        return 1
    if n not in chain_lengths:
        chain_lengths[n] = 1 + chain_length(n // 2 if n % 2 == 0 else 3 * n + 1)
    return chain_lengths[n]

best_n = 0
best_chain_length = 0
for i in range(1, 1000000):
    cl = chain_length(i)
    if cl > best_chain_length:
        best_n, best_chain_length = i, cl
print(best_n, best_chain_length)