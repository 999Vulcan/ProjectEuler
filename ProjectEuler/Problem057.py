"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

 V2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

from fractions import *

cache = {}
def V2(iter):
    if not iter in cache:
        cache[iter] = 2 + Fraction(1, V2(iter-1)) if iter else 2
    return cache[iter]

print(sum(1 if len(str((V2(i)-1).numerator)) > len(str((V2(i)-1).denominator)) else 0 for i in range(1, 1001)))
