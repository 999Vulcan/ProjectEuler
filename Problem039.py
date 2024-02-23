"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
"""

def solutions(p):
    result = 0
    for a in range(1, p//3):
        for b in range(a, (p-a)//2):
            c = p - a - b
            if a**2 + b**2 == c**2:
                result += 1
    return result

result = 0
for i in range(1001):
    sol = solutions(i)
    if sol > result:
        result = sol
        p = i
print(p)
