def sum_of_fifth_powers_of_digits(n):
    return sum(int(digit) ** 5 for digit in str(n))

total = 0
for i in range(10, 354295):  # Start from 10, since single-digit numbers don't count
    if i == sum_of_fifth_powers_of_digits(i):
        total += i

print(total)
