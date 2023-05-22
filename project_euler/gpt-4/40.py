def compute_product():
    decimal_fraction = ""
    i = 1

    # Generate the concatenated decimal fraction
    while len(decimal_fraction) <= 1000000:
        decimal_fraction += str(i)
        i += 1

    # Compute the product
    product = 1
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    for index in indices:
        product *= int(decimal_fraction[index - 1])

    return product

result = compute_product()
print(result)
