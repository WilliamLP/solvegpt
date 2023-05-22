import itertools
import math

def is_square(n):
    return int(math.sqrt(n)) ** 2 == n

def get_word_key(word):
    return ''.join(sorted(word))

words = ['race', 'care', 'face', 'acre', 'fear']  # Replace this list with words from your file

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
        nums = [int(''.join(perm[c] for c in word)) for word in anagram]
        if all(is_square(num) for num in nums):
            max_square = max(max_square, max(nums))

print(max_square)
