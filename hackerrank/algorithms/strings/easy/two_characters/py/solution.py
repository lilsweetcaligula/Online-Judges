#!/bin/python3

import sys

def solution(s):
    import itertools

    chars   = tuple(set(s))
    strings = []

    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            t = ''.join(char for char in s if char in (chars[i], chars[j]))
            
            for char, group in itertools.groupby(t):
                if len(tuple(group)) > 1:
                    break
            else:
                strings.append(t)

    return strings

n        = int(input())
source   = input().strip()
strings  = solution(source)
result   = len(max(strings, key=len)) if strings else 0

print(result)
