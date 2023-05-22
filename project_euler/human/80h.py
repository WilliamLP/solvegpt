import decimal

from euler import *
from decimal import Decimal, getcontext
getcontext().prec = 102

total = 0
for i in range(2, 101):
    if not is_perfect_square(i):
        dgts = str(Decimal(i).sqrt())
        total += sum([int(d) for d in dgts.replace('.', '')[:100]])
print(total)