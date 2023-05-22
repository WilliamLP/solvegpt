def roman_to_int(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total

def int_to_roman(num):
    values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
              (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    for value, letters in values:
        while num >= value:
            roman += letters
            num -= value
    return roman

def count_saved_characters(filename):
    total_saved = 0
    with open(filename, 'r') as file:
        for line in file:
            roman = line.strip()  # remove newline
            num = roman_to_int(roman)
            minimal_roman = int_to_roman(num)
            total_saved += len(roman) - len(minimal_roman)
    return total_saved

filename = 'roman.txt'
print(count_saved_characters(filename))
