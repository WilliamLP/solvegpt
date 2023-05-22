

LIMIT = 50
count = 0
for x1 in range(LIMIT + 1):
    for x2 in range(LIMIT + 1):
        for y1 in range(LIMIT + 1):
            for y2 in range(LIMIT + 1):
                if (x1, y1) == (0, 0) or (x2, y2) == (0, 0) or (x1, y1) >= (x2, y2):
                    continue
                side_sqs = sorted([x1*x1 + y1*y1, x2*x2 + y2*y2,
                            (x2 - x1) ** 2 + (y2 - y1) ** 2])
                if side_sqs[0] + side_sqs[1] == side_sqs[2]:
                    print(x1, y1, '-', x2, y2)
                    count += 1
print(count)