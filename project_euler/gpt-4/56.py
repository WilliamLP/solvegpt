max_digital_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        # Compute a^b
        power = a**b
        # Convert the number to a string, then to a list of integers, then compute the sum of the digits
        digital_sum = sum(int(digit) for digit in str(power))
        # Update max_digital_sum if the current sum is greater
        max_digital_sum = max(max_digital_sum, digital_sum)

print(max_digital_sum)
