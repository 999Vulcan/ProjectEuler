"""
Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

import itertools

keyrange = [ord('a') + i for i in range(27)]
crypt = [int(c) for c in open("Problem059.txt").readline()[:-1].split(',')]

for key in itertools.product(keyrange, keyrange, keyrange):
    text = ''.join([chr(crypt[i] ^ key[i % len(key)]) for i in range(len(crypt))])
    if "world" in text:
        print(sum(ord(text[i]) for i in range(len(text))))
        break
