def get_proper_divisors_sum(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum


def get_abundant_numbers(limit):
    return [n for n in range(12, limit) if get_proper_divisors_sum(n) > n]


def find_non_abundant_sum(limit):
    abundant_numbers = get_abundant_numbers(limit)
    abundant_sums = [False] * (limit + 1)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                abundant_sums[abundant_sum] = True
            else:
                break

    return sum(index for index, is_abundant_sum in enumerate(abundant_sums) if not is_abundant_sum)


limit = 28123
result = find_non_abundant_sum(limit)
print(result)
