def word_value(word):
    return sum(ord(c) - 64 for c in word.upper())

def is_triangle_number(num):
    n = int((-1 + (1 + 8 * num) ** 0.5) / 2)
    return num == n * (n + 1) // 2

def count_triangle_words(filename):
    with open(filename, 'r') as f:
        words = f.read().strip().split(',')
        words = [word.strip('"') for word in words]

    count = 0
    for word in words:
        if is_triangle_number(word_value(word)):
            count += 1

    return count

filename = 'words.txt'
print(count_triangle_words(filename))
