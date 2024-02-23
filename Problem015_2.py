"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

def routes(x, y):
    if x == 0 or y == 0: return(1)
    r = routes(x-1, y) + routes(x, y-1)
    return r

print(routes(20, 20))
