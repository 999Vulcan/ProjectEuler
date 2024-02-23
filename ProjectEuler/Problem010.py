"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import *

def sieve(n):
    s = {i:i for i in range(2, n+1)}
    for i in range(2, round(sqrt(n))+1):
        if i in s:
            for j in range(i * 2, n+1, i):
                if j in s:
                    del s[j]
    return list(s)

print(sum(sieve(2000000)))
