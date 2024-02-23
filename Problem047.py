"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

from math import *

def sieve(n):
    s = {i:i for i in range(2, n+1)}
    for i in range(2, round(sqrt(n))+1):
        if i in s:
            for j in range(i * 2, n+1, i):
                if j in s:
                    del s[j]
    return sorted(s)

def countFactors(n):
    factors = 0
    i = 0
    while n > 1:
        if n % primes[i] == 0:
            factors += 1
            while n % primes[i] == 0:
                n //= primes[i]
        i += 1
    return factors

primes = sieve(1000000)
n = 0
fours = 0
while True:
    n += 1
    if countFactors(n) == 4:
        fours += 1
        if fours == 4:
            break
    else:
        fours = 0
print(n-3)
