"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

perms = []
def lexperm(digits, start):
    if start == len(digits):
        perms.append(digits)
    else:
        for i in range(start, len(digits)):
            lexperm(digits[:start] + digits[i] + digits[start:i] + digits[i+1:], start + 1)
lexperm('0123456789', 0)
print(perms[999999])
