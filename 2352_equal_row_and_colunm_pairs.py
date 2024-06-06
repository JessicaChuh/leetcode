#Given a 0-indexed n x n integer matrix grid, return the number
#of pairs (ri, cj) such that row ri and column cj are equal.

#A row and column pair is considered equal if they contain the
# same elements in the same order (i.e., an equal array).

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

import numpy as np
def equalPairs(grid):
    array_original = np.array(grid)
    array_t = array_original.T

    n_pair = 0
    for i in grid:
        for j in array_t.tolist():
            if i == j:
                n_pair += 1
    return n_pair

print(equalPairs(grid))

## Take away:
# np.unique(grid,axis=0)
#array_t.tolist()
