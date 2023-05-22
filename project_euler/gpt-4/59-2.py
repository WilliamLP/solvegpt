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
from collections import Counter
import re

def is_english(message):
    common_words = set(['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it',
                        'i', 'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this',
                        'they', 'is', 'an', 'at', 'but','we', 'his', 'from', 'that', 'not',
                        'by', 'she', 'or', 'as', 'what', 'go', 'their','can', 'who', 'get',
                        'if', 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will',
                        'as', 'up', 'one', 'time', 'has', 'been', 'there', 'year', 'so',
                        'think', 'when', 'which', 'them', 'some', 'me', 'people', 'take',
                        'out', 'into', 'just', 'see', 'him', 'your', 'come', 'could', 'now',
                        'than', 'like', 'other', 'how', 'then', 'its', 'our', 'two', 'more',
                        'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because',
                        'day', 'more', 'use', 'no', 'man', 'find', 'here', 'thing', 'give',
                        'many', 'well'])

    text = ''.join(message).lower()  # Convert list of characters to lowercase string
    words = re.findall(r'\b\w+\b', text)  # Extract words with regex
    word_count = Counter(words)  # Count the occurrences of each word

    # Check the 20 most common words in the text
    common_in_text = [word for word, _ in word_count.most_common(20)]
    intersection = common_words.intersection(common_in_text)
    if len(intersection) > 10:
        print(intersection)
    # If at least half of the most common words are also common English words, it's probably English
    return len(intersection) > 10



# Try all keys
for key in keys:
    decrypted_message = decrypt(cipher_text, key)
    if is_english(decrypted_message):
        # Print the key and the sum of the ASCII values in the original text
        print('Key:', ''.join(key))
        print('Sum of ASCII values:', sum(ord(char) for char in decrypted_message))
        break
