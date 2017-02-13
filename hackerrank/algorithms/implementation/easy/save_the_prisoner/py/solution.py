testCount = int(input())

for testId in range(testCount):
    n, m, s  = map(int, input().split())
    poisoned = ((s - 1) + (m - 1)) % n + 1
    
    print(poisoned)
