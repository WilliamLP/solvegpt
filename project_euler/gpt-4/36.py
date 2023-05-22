def is_palindrome(n):
    """Returns True if n is a palindrome."""
    return str(n) == str(n)[::-1]

def is_palindrome_base_2(n):
    """Returns True if n is a palindrome in binary."""
    return is_palindrome(bin(n)[2:])

total = 0
for i in range(1, 1000000):
    if is_palindrome(i) and is_palindrome_base_2(i):
        total += i

print(total)
