#!/bin/python3

import sys

cmp         = lambda a, b: (a > b) - (b > a)

aliceScores = tuple(map(int, input().strip().split(' ')))
bobScores   = tuple(map(int, input().strip().split(' ')))

scoreCmp    = tuple(map(lambda a, b: cmp(a, b), aliceScores, bobScores))
aliceScore  = len(tuple(filter(lambda x: x > 0, scoreCmp)))
bobScore    = len(tuple(filter(lambda x: x < 0, scoreCmp)))

print(aliceScore, bobScore)
