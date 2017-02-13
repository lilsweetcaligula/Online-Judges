#!/bin/python3

import sys


def solution(b):
    count = 0

    for i in range(len(b)):
        if b[i] % 2:
            b[i]  += 1
            count += 1

            if i < len(b) - 1:
                b[i + 1] += 1
                count += 1
            elif i > 0:
                b[i - 1] += 1
                count += 1

    if any(x % 2 for x in b):
        return None

    return count

N = int(input())
B = list(map(int, input().split()))
c = solution(B)

if c != None:
    print(c)
else:
    print('NO')
