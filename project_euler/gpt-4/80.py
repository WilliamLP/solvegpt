import decimal
from decimal import Decimal

# Set the precision to calculate up to 101 decimal places
decimal.getcontext().prec = 101

def digital_sum(n):
    """Calculate the sum of the digits in a number."""
    return sum(int(digit) for digit in str(n) if digit not in ['.', '-'])

# Compute the sum of the first 100 decimal places for all square roots from 1 to 100
total = 0
for n in range(1, 101):
    root = Decimal(n).sqrt()
    if not root % 1 == 0:
        total += digital_sum(str(root)[:101])  # include the integer part

print(total)
