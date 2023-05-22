import itertools
import operator
import sys

def expressions(nums):
    if len(nums) == 1:
        yield nums[0], str(nums[0])
    else:
        for i in range(1, len(nums)):
            for left in expressions(nums[:i]):
                for right in expressions(nums[i:]):
                    yield left[0] + right[0], '({} + {})'.format(left[1], right[1])
                    yield left[0] - right[0], '({} - {})'.format(left[1], right[1])
                    yield left[0] * right[0], '({} * {})'.format(left[1], right[1])
                    if right[0] != 0:
                        yield left[0] / right[0], '({} / {})'.format(left[1], right[1])

def consecutive_values(nums):
    generated = set()
    for nums_permutation in itertools.permutations(nums, len(nums)):
        for value, _ in expressions(nums_permutation):
            if value > 0 and value == int(value):
                generated.add(int(value))
    consecutive = 0
    while consecutive + 1 in generated:
        consecutive += 1
    return consecutive

best_nums = []
best_consecutive = 0

for digits in itertools.combinations(range(0, 10), 4):
    consecutive = consecutive_values(digits)
    if consecutive > best_consecutive:
        best_consecutive = consecutive
        best_nums = digits

print("".join(map(str, sorted(best_nums))))
