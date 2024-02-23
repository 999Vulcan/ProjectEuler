"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

f1, f2 = 1, 1
n = 2
while len(str(f2)) < 1000:
    f1, f2 = f2, f1 + f2
    n += 1
print(n)
