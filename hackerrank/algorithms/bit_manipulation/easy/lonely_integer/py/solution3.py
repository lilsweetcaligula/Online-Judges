#!/usr/bin/py

def lonelyinteger(a):
    answer = 0
    nums = {}
    for value in a:
        if value in nums:
            nums[value] += 1
        else:
            nums[value] = 1
    for value in a:
        if nums[value] < 2:
            answer = value
            break
    return answer
    
a = input()
b = map(int, raw_input().strip().split(" "))
print lonelyinteger(b)
