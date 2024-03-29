"""
Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70  22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk  Pj| is minimised; what is the value of D?
"""

def findD(pnumbers):
    for d in sorted(pnumbers):
        for i in pnumbers:
            if i + d in pnumbers and 2*i + d in pnumbers:
                return(d)

print(findD({n*(3*n-1)//2 for n in range(1, 10000)}))
