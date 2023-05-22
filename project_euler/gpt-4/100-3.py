def find_blue_disks():
    x, y = 1, 1
    while True:
        x_next = 3*x + 4*y
        y_next = 2*x + 3*y
        x, y = x_next, y_next
        if (x + y) > 10**12:  # (x+y) gives total disks as x gives blue disks and y gives red disks
            return x  # x gives the count of blue disks

print(find_blue_disks())
