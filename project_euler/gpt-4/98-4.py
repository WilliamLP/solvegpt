import itertools
import math

def is_square(n):
    return int(math.sqrt(n)) ** 2 == n

def get_word_key(word):
    return ''.join(sorted(word))

with open('words.txt', 'r') as f:
    words = f.readline().replace('"', '').lower().split(',')

anagrams = {}
for word in words:
    key = get_word_key(word)
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]

max_square = 0
for anagram in anagrams.values():
    if len(anagram) < 2:
        continue
    for perm in itertools.permutations('1234567890', len(anagram[0])):
        letter_to_digit = {letter: digit for letter, digit in zip(anagram[0], perm)}
        str_nums = [''.join(letter_to_digit[c] for c in word) for word in anagram]
        if any(str_num[0] == '0' for str_num in str_nums):
            continue
        nums = [int(str_num) for str_num in str_nums]
        if all(is_square(num) for num in nums):
            print(anagram, nums)
            max_square = max(max_square, max(nums))

print(max_square)
