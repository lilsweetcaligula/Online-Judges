#!/bin/python3

import sys

PENALTY_THUNDERBOLT = 2
PENALTY_JUMP        = 1

e    = 100

n, k = input().strip().split(' ')
n, k = [int(n),int(k)]
c    = [int(c_temp) for c_temp in input().strip().split(' ')]

i    = 0

while True:
    if c[i]:
        e -= PENALTY_THUNDERBOLT
    
    i  = (i + k) % n
    e -= PENALTY_JUMP
    
    if i == 0:
        break
        
print(e)
