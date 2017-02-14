#!/bin/python

def countingSort(L, lo, hi, key=lambda x : x):
    if lo >= hi:
        return
        
    maxKey = minKey = key(L[lo])
    
    for i in range(lo, hi):
        item = L[i]
        itemKey = key(item)
        if itemKey > maxKey:
            maxKey = itemKey
        elif itemKey < minKey:
            minKey = itemKey
            
    counts = [0] * (maxKey + 1 - minKey)
    
    for i in range(lo, hi):
        item = L[i]
        counts[key(item) - minKey] += 1
        
    total = 0
    
    for i in range(len(counts)):
        oldCount = counts[i]
        counts[i] = total
        total += oldCount
        
    output = [None] * (len(L[lo:hi]))
    
    for i in range(lo, hi):
        item = L[i]
        output[counts[key(item) - minKey]] = item
        counts[key(item) - minKey] += 1
        
    L[lo:hi] = output[:]
    
entryCount = int(raw_input())
entries = []

for entryId in range(entryCount):
    key, value = raw_input().split()
    entry = [int(key), value]
    entries.append(entry)
    
for i in range(len(entries)):
    if i < len(entries) // 2:
        entries[i].append(False)
    else:
        entries[i].append(True)
        
countingSort(entries, 0, len(entries), key=lambda entry : entry[0])
for entry in entries:
    if entry[2] == True:
        print entry[1],
    else:
        print '-',
        
