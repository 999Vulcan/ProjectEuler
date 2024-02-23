"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from fractions import *
product = Fraction(1)

for i in range(11,99):
    for j in range (i+1, 100):
        if i%10 and j%10 and \
        ((i/j == int(str(i)[0]) / int(str(j)[1]) and int(str(i)[1]) == int(str(j)[0])) or \
        (i/j == int(str(i)[1]) / int(str(j)[0]) and int(str(i)[0]) == int(str(j)[1]))):
            product *= Fraction(i,j)

print(product.denominator)
