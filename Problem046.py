"""
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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

for n in range(9, 1000000, 2):
    if n in primes: continue
    i = 0
    while 2*i**2 < n:
        i += 1
        if n - 2*i**2 in primes:
            break
    else:
        print(n)
