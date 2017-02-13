#!/bin/python3

import sys

# The cmp function has been removed from Python 3.x so we define it here
# ourselves.
# [href.] https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons
#   "If you really need the cmp() functionality, you could use the expression 
#    (a > b) - (a < b) as the equivalent for cmp(a, b)."
#
cmp         = lambda a, b: (a > b) - (a < b)

aliceScores = tuple(map(int, input().strip().split(' ')))
bobScores   = tuple(map(int, input().strip().split(' ')))

scoreCmp    = tuple(map(lambda a, b: cmp(a, b), aliceScores, bobScores))
aliceScore  = len(tuple(filter(lambda x: x > 0, scoreCmp)))
bobScore    = len(tuple(filter(lambda x: x < 0, scoreCmp)))

print(aliceScore, bobScore)
