import math

def find_blue_disks():
    x = 1
    y = 1
    while True:
        x_next = 3*x + 4*y
        y_next = 2*x + 3*y
        x, y = x_next, y_next

        total_disks = y + 1
        if total_disks > 10**12:
            return (x+1)//2

print(find_blue_disks())
