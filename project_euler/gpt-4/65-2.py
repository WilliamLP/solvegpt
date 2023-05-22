def e_convergent_fraction(k):
    p, q = [1, 2], [0, 1]  # base cases
    for i in range(2, k + 1):
        if i % 3 != 2:
            a = 1
        else:
            a = 2 * (i // 3 + 1)
        p.append(a * p[-1] + p[-2])
        q.append(a * q[-1] + q[-2])
    return p[k], q[k]

# The 10th convergent of the continued fraction for e
numerator_10, denominator_10 = e_convergent_fraction(9)
print(f"{numerator_10}/{denominator_10}")
