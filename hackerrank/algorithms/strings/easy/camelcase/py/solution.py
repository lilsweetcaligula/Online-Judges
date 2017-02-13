#!/bin/python3

import sys

def camelCaseWordCount(s):    
    count = 0
    
    if not s[0].isupper():
        count += 1
        
    return count + len([char for char in s if char.isupper()])

s = input().strip()

print(camelCaseWordCount(s))
