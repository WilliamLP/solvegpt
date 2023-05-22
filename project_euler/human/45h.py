limit = 10000000000
penta, hexa = set(), set()

i = 1
while True:
    num = i * (3 * i - 1) // 2
    if num > limit:
        break
    penta.add(num)
    i += 1

i = 1
while True:
    num = i * (2 * i - 1)
    if num > limit:
        break
    hexa.add(num)
    i += 1


i = 1
while True:
    num = i * (i + 1) // 2
    if num > limit:
        break
    if num in penta and num in hexa:
        print(num)
    i += 1

