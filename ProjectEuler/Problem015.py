"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

cache = {}

def routes(x, y):
    if (x, y) in cache: return cache[(x,y)]
    if x*y == 0: return(1)
    cache[(x,y)] = routes(x-1, y) + routes(x, y-1)
    return cache[(x,y)]

print(routes(20, 20))
