from itertools import count

def product_sum_numbers(limit):
    # Initialize an array to keep track of the minimal product-sum number for each k value.
    result = [None] * (limit + 1)
    max_k = 0

    def search(n, k, sum_, prod):
        nonlocal max_k
        if k > max_k and sum_ == prod and n <= limit:
            result[n] = prod
            max_k = k
        if k + 1 > max_k and sum_ + 1 == prod and n + 1 <= limit:
            result[n + 1] = prod
            max_k = k + 1
        if max_k < limit and n * 2 <= limit:
            search(n * 2, k + 1, sum_ + 2, prod * 2)

    for i in count(2):
        if result.count(None) == 1:
            break
        search(i, 1, i, i)

    return sum(set(result[2:]))

# Call the function with the specified limit
print(product_sum_numbers(12000))
