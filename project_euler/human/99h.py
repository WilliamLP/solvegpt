import math
best_line_num, best_val = None, 0
with open('base_exp.txt', 'r') as f:
    for i, l in enumerate(f):
        nums = [int(n) for n in l.split(',')]
        val = math.log(nums[0]) * nums[1]
        if val > best_val:
            best_line_num, best_val = i + 1, val
print(best_line_num)