"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from math import *
from itertools import *

"""
def isPandigital(s):
    return ''.join(sorted(list(s))) == '123456789'[:len(s)]
"""

def isPrime(n):
    for i in range(2, round(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

products = set()
n = 4
for i in range(6):
    if isPrime(n):
        break
    for perm in permutations('7654321'[i:]):
        n = int(''.join(perm))
        if isPrime(n):
            break
print(n)
