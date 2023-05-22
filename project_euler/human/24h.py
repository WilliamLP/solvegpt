def _permutations(nums):
    if len(nums) == 1:
        return [[nums[0]]]
    result = []
    for i in range(len(nums)):
        first = [nums[i]]
        rest = [nums[j] for j in range(len(nums)) if j != i]
        result.extend([first + p for p in _permutations(rest)])
    return result

def permutations(n):
    return _permutations([i for i in range(n)])

ps = permutations(10)[1000000 - 1]
print(''.join(str(p) for p in ps))
