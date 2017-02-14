#!/usr/bin/py

def lonelyinteger(a):
    return reduce(lambda x,y : x ^ y, a)

a = input()
b = map(int, raw_input().strip().split(" "))
print lonelyinteger(b)
