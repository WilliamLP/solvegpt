import itertools
import string

# Read the cipher text from the file
with open('p059_cipher.txt') as f:
    cipher_text = list(map(int, f.read().strip().split(',')))

# Generate all possible 3-character lowercase keys
keys = list(itertools.product(string.ascii_lowercase, repeat=3))

# Function to decrypt a message using a key
def decrypt(cipher_text, key):
    key_length = len(key)
    return [chr(cipher_text[i] ^ ord(key[i % key_length])) for i in range(len(cipher_text))]

# Function to check if a decrypted message contains common English words
def is_english(message, word_length=5, threshold=0.1):
    words = ''.join(message).split()
    english_words = [word for word in words if len(word) >= word_length]
    return len(english_words) / len(words) >= threshold

# Try all keys
for key in keys:
    decrypted_message = decrypt(cipher_text, key)
    if is_english(decrypted_message):
        # Print the key and the sum of the ASCII values in the original text
        print('Key:', ''.join(key))
        print('Sum of ASCII values:', sum(ord(char) for char in decrypted_message))
        break
