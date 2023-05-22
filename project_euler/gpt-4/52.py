def find_smallest_int():
    x = 1
    while True:
        if sorted(str(x)) == sorted(str(2*x)) == sorted(str(3*x)) == sorted(str(4*x)) == sorted(str(5*x)) == sorted(str(6*x)):
            return x
        x += 1

print(find_smallest_int())
