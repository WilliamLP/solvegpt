def sum_of_multiples(limit, multiples):
    return sum(x for x in range(limit) if any(x % m == 0 for m in multiples))

if __name__ == "__main__":
    limit = 1000
    multiples = [3, 5]
    result = sum_of_multiples(limit, multiples)
    print(f"The sum of all the multiples of 3 or 5 below {limit} is: {result}")
