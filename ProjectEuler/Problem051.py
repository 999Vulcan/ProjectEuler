"""
By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from math import *
from itertools import *

def sieve(n):
    s = {i for i in range(2, n+1)}
    for i in range(2, round(sqrt(n))+1):
        if i in s:
            for j in range(i*2, n+1, i):
                if j in s:
                    s -= {j}
    return s

primeset = sieve(1000000)
primes = sorted(primeset)

def replaceDigits(s, digits, i):
    for digit in digits:
        s = s[:digit] + str(i) + s[digit+1:]
    return s

def findPrimes(n, digits):
    primes = []
    for i in range(10):
        s = str(n)
        s = replaceDigits(s, digits, i)
        if int(s) in primeset and len(s) == len(str(int(s))):
            primes.append(int(s))
    return primes

def findFamily(n, length):
    s = str(n)
    allDigits = [i for i in range(len(s))]
    for i in range(2, len(s)-1):
        for digits in combinations(allDigits, i):
            p = findPrimes(n, digits)
            if len(p) == length:
                print(p[0])
                return True
    return False

for prime in primes:
    if findFamily(prime, 8):
        break
