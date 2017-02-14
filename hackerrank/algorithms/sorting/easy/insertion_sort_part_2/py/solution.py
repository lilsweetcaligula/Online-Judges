#!/bin/python

def insertionSort(ar):    
    DBG = True
    first = True
    for i in xrange(len(ar)):
        key = ar[i]
        for j in reversed(xrange(i)):
            if ar[j] < key:
                break
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
        if DBG and not first: print " ".join(str(value) for value in ar)
        first = False

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
