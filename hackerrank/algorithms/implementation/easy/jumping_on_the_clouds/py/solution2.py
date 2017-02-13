#!/bin/python3

import sys


def solution(clouds):
    import collections

    queue    = collections.deque((0,))
    counts   = collections.deque((0,))
    mincount = None
    
    while len(queue) > 0:
        index = queue.popleft()
        count = counts.popleft()
        
        if index + 1 == len(clouds):
            if mincount == None:
                mincount = count
            else:
                mincount = min(mincount, count)
        elif index < len(clouds) and not clouds[index]:
            for step in (1, 2):
                if index + step <= len(clouds):
                    queue.append(index + step)
                    counts.append(count + 1)
            
    return mincount

n   = int(input().strip())
c   = [int(c_temp) for c_temp in input().strip().split(' ')]

res = solution(c)

print(res)
