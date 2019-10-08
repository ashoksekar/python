#!/usr/bin/python

import math
import os
import random
import re
import sys
import copy

debug = False

full_grid = []
r = c = n = 0
def pop_nuke_grid(grid):
    grid1 = copy.deepcopy(grid)
    for row in xrange(r):
        for col in xrange(c):
            if grid[row][col] == 'O':
                if (col - 1 >= 0):
                    s = list(grid1[row])
                    s[col-1] = 'O'
                    grid1[row] = "".join(s)
                if (col + 1 < c):
                    s = list(grid1[row])
                    s[col+1] = 'O'
                    grid1[row] = "".join(s)
                if (row - 1 >= 0):
                    s = list(grid1[row-1])
                    s[col] = 'O'
                    grid1[row-1] = "".join(s)
                if (row + 1 < r):
                    s = list(grid1[row+1])
                    s[col] = 'O'
                    grid1[row+1] = "".join(s)
    return grid1

def clear_nuke_grid(grid, nuke_grid):
    for row in xrange(r):
        for col in xrange(c):
            if (nuke_grid[row][col] == 'O'):
                s = list(grid[row])
                s[col] = '.'
                grid[row] = "".join(s)
    return grid
# Complete the bomberMan function below.
def bomberMan(n, grid):
    for i in xrange(n):
        if ((i % 2) == 0):
            nuke_grid = pop_nuke_grid(grid)
            grid = copy.deepcopy(full_grid)
            if (debug):
                print '\n'.join(grid)
                print '\n'
        elif ((i % 2) == 1):
            grid = clear_nuke_grid(grid, nuke_grid)
            if (debug):
                print '\n'.join(grid)
                print '\n'
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = raw_input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in xrange(r):
        grid_item = raw_input()
        grid.append(grid_item)
        full_grid.append("O"*c)

    n %= 24
    result = bomberMan(n-1, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

