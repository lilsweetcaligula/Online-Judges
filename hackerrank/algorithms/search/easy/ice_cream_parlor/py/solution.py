#!/bin/python

def PickIceCream(amount, prices):
    for i in range(len(prices)):
        price = prices[i]
        target = amount - price
        for j in range(len(prices)):
            if i != j and prices[j] == target:
                return i + 1, j + 1
    return ()

testCount = int(raw_input())
for testId in range(testCount):
    amount = int(raw_input())
    size   = int(raw_input())
    prices = [int(value) for value in raw_input().split()]
    picked = PickIceCream(amount, prices)
    print " ".join(str(value) for value in picked)
