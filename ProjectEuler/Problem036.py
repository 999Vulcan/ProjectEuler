"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isPalindromic(n):
    return n == n[::-1]

s = 0
for i in range(1000000):
    if isPalindromic(str(i)) and isPalindromic(bin(i)[2:]):
        s += i

print(s)
