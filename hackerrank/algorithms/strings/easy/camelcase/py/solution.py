#!/bin/python3

import sys

def camelCaseWordCount(s):
    return 1 + len([c for c in s if c.isupper()])

s     = input().strip()
count = camelCaseWordCount(s)

print(count)
