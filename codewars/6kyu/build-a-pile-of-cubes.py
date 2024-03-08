# Trouble copying the formulas in from the kata description.
# URL: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python

def find_nb(m):
    total = 0
    n = 0
    # Keep adding cubes to you either hit m or go past it
    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1