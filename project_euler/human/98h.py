
from collections import defaultdict
from itertools import combinations

def anagram_pairs(words):
    anagram_grps = defaultdict(list)
    for word in words:
        anagram_grps[''.join(sorted([ch for ch in word]))].append(word)
    result = []
    for grp in anagram_grps.values():
        if len(grp) == 1:
            continue
        result.extend(combinations(grp, 2))  # Get pairs if group size > 2
    return result

def test_pairs(pair1, pair2):
    mp = {}
    for i, ch in enumerate(pair1[0]):  # Build the map
        if ch in mp and pair2[0][i] != ch:
            return False  # Duplicate letter must match duplicate digit in square
        mp[ch] = pair2[0][i]
    #if len(set(mp.values())) != len(mp.values()):
    #    return False  # Must be 1-1 map
    for i, ch in enumerate(pair1[1]):  # Apply the map to the second word and test
        if mp[ch] != pair2[1][i]:
            return False
    return True

TEST_LENGTH = 8

with open('words.txt', 'r') as f:
    words = f.readline().replace('"', '').split(',')

word_pairs = anagram_pairs([word for word in words if len(word) == TEST_LENGTH])

sq_words = [str(i*i) for i in range(1, int(10**(TEST_LENGTH/2)) + 1)]
sq_pairs = anagram_pairs([word for word in sq_words if len(word) == TEST_LENGTH])
print(sq_pairs)
largest_sq = 0
for word_pair in word_pairs:
    for sq_pair in sq_pairs:
        if test_pairs(word_pair, sq_pair) or test_pairs(word_pair[::-1], sq_pair):
            print(word_pair, sq_pair)
            largest_sq = max(largest_sq, int(sq_pair[0]), int(sq_pair[1]))
print(largest_sq)