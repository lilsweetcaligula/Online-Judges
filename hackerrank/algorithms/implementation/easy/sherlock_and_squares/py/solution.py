def countSquareNumbersInRange(lowerBound, upperBound):
    import math
    
    power = math.ceil(math.sqrt(lowerBound))
    count = 0
    
    while power ** 2 < upperBound:
        power += 1
        count += 1
        
    return count

testCount = int(input())

for testId in range(testCount):
    first, last = map(int, input().split())
    count       = countSquareNumbersInRange(first, last + 1)
    
    print(count)
