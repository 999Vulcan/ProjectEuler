"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from math import *

def sieve(n):
    s = {i:i for i in range(2, n+1)}
    for i in range(2, round(sqrt(n))+1):
        if i in s:
            for j in range(i * 2, n+1, i):
                if j in s:
                    del s[j]
    return s

def circular(n):
    s = str(n)
    for i in range(len(s)):
        s = s[1:] + s[0]
        if not int(s) in primes:
            return False
    return True

primes = sieve(1000000)
circulars = 0

for n in primes:
    if circular(n):
        circulars += 1

print(circulars)
