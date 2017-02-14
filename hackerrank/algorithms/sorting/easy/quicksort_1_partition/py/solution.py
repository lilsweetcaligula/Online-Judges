#!/bin/python

def partition(ar):
    i = lt = 0
    gt = len(ar) - 1
    pivot = ar[0]
    while i <= gt:
        if ar[i] < pivot:
            ar[i], ar[lt] = ar[lt], ar[i]
            lt += 1
            i += 1
        elif ar[i] > pivot:
            ar[i], ar[gt] = ar[gt], ar[i]
            gt -= 1
        else:
            i += 1
    return lt
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
j = partition(ar)
print " ".join(str(value) for value in ar)
