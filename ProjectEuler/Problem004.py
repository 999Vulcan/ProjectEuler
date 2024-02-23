"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = 0
for i in range (101, 999):
    for j in range (100, i):
        if str(i*j) == str(i*j)[::-1]:
           palindrome = max(i*j, palindrome)
print(palindrome)
