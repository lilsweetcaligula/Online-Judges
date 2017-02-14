#!/bin/python

def insertion_sort(L):
    for i in xrange(1, len(L)):
        j = i - 1
        key = L[i]
        while (j >= 0) and (L[j] > key):
           L[j+1], L[j] = L[j], L[j + 1]
           j -= 1

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
