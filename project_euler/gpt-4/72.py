def compute_totients(limit):
    phi = list(range(limit+1))
    for i in range(2, limit+1):
        if phi[i] == i:  # i is a prime
            for j in range(i, limit+1, i):
                phi[j] -= phi[j] // i
    return phi

def count_fractions(limit):
    totients = compute_totients(limit)
    return sum(totients) - 1  # subtract 1 to exclude the fraction 1/1

print(count_fractions(1000000))
