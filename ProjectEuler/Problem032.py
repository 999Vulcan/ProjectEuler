"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import *
products = set()
for perm in permutations('123456789'):
    s = ''.join(perm)
    for i in range(1,4):
        for j in range(i+2,7):
            if int(s[:i])*int(s[i:j]) == int(s[j:]):
                products.add(int(s[j:]))
print(sum(products))
