def solution(source):
    import collections
    
    counter  = collections.Counter(source)    
    parities = tuple(counter[char] % 2 == 0 for char in counter)
        
    if len(source) % 2:
        return parities.count(False) == 1
   
    return all(parities)

s = input().strip()

if solution(s):
    print('YES')
else:
    print('NO')
