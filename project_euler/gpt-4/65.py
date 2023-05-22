def e_convergent_numerator(k):
    p = [2, 3]  # p_0 and p_1
    for i in range(2, k + 1):
        if i % 3 != 2:
            a = 1
        else:
            a = 2 * (i // 3 + 1)
        p.append(a * p[-1] + p[-2])
    return p[k]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# The sum of digits in the numerator of the 100th convergent
numerator_100 = e_convergent_numerator(10)
sum_of_digits_100 = sum_of_digits(numerator_100)
print(sum_of_digits_100)
