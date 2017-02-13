#!/bin/python3

import sys

def solution(board):
    import collections
    
    count = 1

    for pos in range(1, len(board) + 1):
        if pos == len(board) or board[pos] != board[pos - 1]:
            if count < 2:
                break
            count = 1
        else:
            count += 1
    else:
        return True

    ladybugs = ''.join(x for x in board if x != '_')
    counts   = collections.Counter(ladybugs)
    
    for x in counts:
        if counts[x] < 2:
            return False
        
    return len(board) - len(ladybugs) > 0

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    
    if solution(b):
        print('YES')
    else:
        print('NO')
        
