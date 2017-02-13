#!/bin/python3

import sys

def solution(s, k):
    def shiftLetter(letter, k):
        import string

        if k > 0:
            if letter.isupper():
                return string.ascii_uppercase[(k + (ord(letter) - ord('A'))) % len(string.ascii_uppercase)]
            else:
                return string.ascii_lowercase[(k + (ord(letter) - ord('a'))) % len(string.ascii_lowercase)]

        if letter.isupper():
            return string.ascii_uppercase[(len(string.ascii_uppercase) + k + (ord(letter) - ord('A'))) % len(string.ascii_uppercase)]

        return string.ascii_lowercase[(len(string.ascii_lowercase) + k + (ord(letter) - ord('a'))) % len(string.ascii_lowercase)]
        
        
    return ''.join(shiftLetter(c, k) if c.isalpha() else c for c in s)
        

n = int(input())
s = input().strip()
k = int(input())
t = solution(s, k)

print(t)
