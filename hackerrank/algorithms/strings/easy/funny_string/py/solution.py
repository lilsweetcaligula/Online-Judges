def isFunny(s):
    r = s[::-1]
    i = 1
    
    while i < len(s):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return False        
        i += 1
    
    return True

testCount = int(input())

for testId in range(testCount):
    source = input().strip()
    
    if isFunny(source):
        print('Funny')
    else:
        print('Not Funny')
       
