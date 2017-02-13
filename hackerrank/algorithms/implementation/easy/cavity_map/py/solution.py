#!/bin/python3

import sys

def isCavity(lookup, i, j):
    if not 0 < i < len(lookup) - 1:
        return False

    if not 0 < j < len(lookup[0]) - 1:
        return False

    top,  bottom = i - 1, i + 1
    left, right  = j - 1, j + 1

    for x in range(top, bottom + 1):
        if x != i and lookup[x][j] >= lookup[i][j]:
            return False

    for x in range(left, right + 1):
        if x != j and lookup[i][x] >= lookup[i][j]:
            return False

    return True

def findCavities(lookup):
    result = []

    for i in range(len(lookup)):
        for j in range(len(lookup)):
            if isCavity(lookup, i, j):
                result.append((i, j))

    return result

n      = int(input().strip())
grid   = []
grid_i = 0

for grid_i in range(n):
   grid_t = tuple(map(int, input().strip()))
   grid.append(grid_t)
    
cavPoses = set(findCavities(grid))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in cavPoses:
            print('X', end='')
        else:
            print(grid[i][j], end='')
    print()
