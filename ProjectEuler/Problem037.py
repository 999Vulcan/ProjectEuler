"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

primes = sieve(1000000)
n = 0
result = 0

def isTruncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not (int(s[i:]) in primes and int(s[:i]) in primes):
            return False        
    return True

for prime in primes:
    if isTruncatable(prime):
        n += 1
        result += prime
        if n == 15:
            break
print(result-7-5-3-2)
