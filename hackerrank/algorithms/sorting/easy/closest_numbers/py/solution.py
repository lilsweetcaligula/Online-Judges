#!/bin/python

size = int(raw_input())
values = sorted([int(value) for value in raw_input().split()][:size])
differences = sorted([(values[i - 1], values[i]) for i in range(1, len(values))], key = lambda x : abs(x[0] - x[1]))
i = 1
while (i < len(differences) 
    and abs(differences[i][0] - differences[i][1]) == abs(differences[i - 1][0] - differences[i - 1][1])):
    i += 1
smallestDifferences = differences[:i]
print " ".join(" ".join(str(value) for value in difference) for difference in smallestDifferences)
