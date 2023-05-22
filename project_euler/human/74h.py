import math

chain_lengths = [0 for i in range(3000000)]
chain_lengths[1] = chain_lengths[2] = chain_lengths[145] = 1
chain_lengths[169] = chain_lengths[363601] = chain_lengths[1454] = 3
chain_lengths[871] = chain_lengths[45361] = 2
chain_lengths[871] = chain_lengths[45362] = 2

def get_chain_length(n, depth):
    if depth == 0:
        return 1  # We don't need to go past depth 60
    if not chain_lengths[n]:
        new_n = sum([math.factorial(int(ch)) for ch in str(n)])
        chain_lengths[n] = 1 + get_chain_length(new_n, depth - 1)
    return chain_lengths[n]

for n in range(1000000):
    get_chain_length(n, 61)

print(len([n for n in range(1000000) if chain_lengths[n] == 60]))