from euler import *

best = ''
for p in permutations(9):
    outer = [10] + [d+1 for d in p[:4]]
    inner = [d+1 for d in p[4:]]

    sums = set()
    for i, o in enumerate(outer):
        sm = o + inner[i] + inner[(i+1) % 5]
        sums.add(sm)
    if len(sums) == 1:  # magic ring
        start_i = [i for i in range(5) if outer[i] == min(outer)][0]
        st = ''
        for i in range(5):
            st += str(outer[(start_i + i) % 5])\
                  + str(inner[(start_i + i) % 5])\
                  + str(inner[(start_i + i + 1) % 5])
        best = max(st, best)
print(best)

"""
  4
   \
    3
   / \
  1---2-6
 /
5
"""