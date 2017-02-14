#!/usr/bin/py

def lonelyinteger(a):        
    a.sort()
    answer = 0
    count = 1
    i = 1
    while i < len(a):
        if a[i - 1] == a[i]:
            count += 1
        elif count < 2:
            answer = a[i - 1]
            break
        else:
            count = 1
        i += 1
    if count < 2:
        answer = a[i - 1]
    return answer

a = input()
b = map(int, raw_input().strip().split(" "))
print lonelyinteger(b)
