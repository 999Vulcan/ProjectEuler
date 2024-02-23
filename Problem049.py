"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from math import *
from itertools import *

def sieve(n):
    s = {i:i for i in range(2, n+1)}
    for i in range(2, round(sqrt(n))+1):
        if i in s:
            for j in range(i * 2, n+1, i):
                if j in s:
                    del s[j]
    return s

def arePerm(*s):
    return all(''.join(sorted(list(str(s[0])))) == ''.join(sorted(list(str(s[i])))) for i in range(len(s)))

primes = sorted(set(sieve(9999)) - set(sieve(999)))

for a, b in combinations(primes, 2):
    c = 2*b-a
    if arePerm(a, b, c) and a in primes and b in primes and c in primes:
        print(str(a)+str(b)+str(c))

