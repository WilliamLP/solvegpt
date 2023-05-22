import math

# maximum denominator
d_max = 10**6

# target fraction is 3/7
target_n, target_d = 3, 7

# start with fraction 0/1
n, d = 0, 1

while d <= d_max:
    # find the fraction to the left of target_n/target_d in the Farey sequence of order d
    n_next = math.floor((d_max - 1) * target_n / target_d)
    d_next = math.floor(d_max / ((target_n / target_n) - (n / d)))

    # update n and d
    n, d = n_next, d_next

print(n, d)
