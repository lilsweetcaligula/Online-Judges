#!/bin/python3

import sys
import datetime

def computeFine(expected, actual):
    if actual.year > expected.year:
        return 10000
    elif actual.year == expected.year:
        if actual.month > expected.month:
            return 500 * abs(actual.month - expected.month)
        elif actual.month == expected.month:
            if actual.day > expected.day:
                return 15 * abs(actual.day - expected.day)
    return 0

actual   = datetime.datetime(*reversed(tuple(map(int, input().split()))))
expected = datetime.datetime(*reversed(tuple(map(int, input().split()))))
fine     = computeFine(expected, actual)

print(fine)
