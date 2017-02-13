#!/bin/python3

import sys


def solution(grid, pattern):
    for i in range(len(grid)):
        if len(grid) - i < len(pattern):
            break
                
        offsets = set()
        offset  = grid[i].find(pattern[0])

        while offset >= 0:
            offsets.add(offset)
            offset = grid[i].find(pattern[0], offset + 1)

        for offset in offsets:
            k = i
            j = 0

            while j < len(pattern):
                curoffset = grid[k].find(pattern[j], offset)

                if curoffset != offset:
                    break

                k += 1
                j += 1

            if j == len(pattern):
                return i, offset

    return ()

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
        
    if solution(G, P):
        print('YES')
    else:
        print('NO')
