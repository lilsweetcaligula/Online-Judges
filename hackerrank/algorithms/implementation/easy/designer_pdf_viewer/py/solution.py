#!/bin/python3

import sys
import string

SEPARATOR    = ' '
LETTER_WIDTH = 1

heights = [int(h_temp) for h_temp in input().strip().split(SEPARATOR)]
word    = input().strip()

width   = len(word) * LETTER_WIDTH
height  = max(heights[ord(letter) - ord('a' if letter.islower() else 'A')] for letter in word)

area    = width * height

print(area)
