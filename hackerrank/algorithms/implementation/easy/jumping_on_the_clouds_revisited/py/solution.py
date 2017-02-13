#!/bin/python3

import sys

PENALTY_THUNDERBOLT = 2
PENALTY_JUMP        = 1

e    = 100

n, k = map(int, input().split())
c    = tuple(map(int, input().split()))
i    = 0

while True:
    if c[i]:
        e -= PENALTY_THUNDERBOLT
    
    i  = (i + k) % n
    e -= PENALTY_JUMP
    
    if i == 0:
        break
        
print(e)
