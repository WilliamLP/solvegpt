def sum_of_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def find_amicable_numbers(limit):
    amicable_numbers = []
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_numbers.append(a)
    return amicable_numbers

limit = 1000000
amicable_numbers = find_amicable_numbers(limit)
result = sum(amicable_numbers)
print("The sum of all amicable numbers under 10000 is:", result)
