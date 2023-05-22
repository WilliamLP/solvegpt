


def decode(input, key):
    output = ''
    for i, n in enumerate(input):
        key_char = ord(key[i % len(key)])
        output += chr(n ^ key_char)
    return output

def run(input):
    letters = [chr(ord('a') + i) for i in range(26)]
    for l1 in letters:
        for l2 in letters:
            for l3 in letters:
                key = l1 + l2 + l3
                decoded = decode(input, key)
                if ' the ' in decoded and ' and ' in decoded:
                    print(decoded, sum([ord(ch) for ch in decoded]))
                    return

input = [int(n) for n in open("p059_cipher.txt", "r").read().split(',')]
run(input)

