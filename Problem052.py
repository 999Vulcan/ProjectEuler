"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

n = 0
while True:
    n += 1
    for i in range(2, 7):
        if sorted(str(n)) != sorted(str(n*i)):
            break
    else:
        print(n)
        break
