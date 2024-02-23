"""
Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from math import *

def sieve(n):
    s = [0 ,0] + [1]*(n+1)
    for i in range(2, round(sqrt(n))+1):
        if s[i]:
            for j in range(i * 2, n+1, i):
                s[j] = 0
    return s

def countPrimes(a, b):
    n = 0
    while True:
        if not s[n**2 + a*n + b]:
            return n
        n += 1

maxa, maxb, maxn = -1000, -1000, 0
s = sieve(1100000)

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = countPrimes(a, b)
        if n > maxn:
            maxa, maxb, maxn = a, b, n

print(maxa * maxb)
