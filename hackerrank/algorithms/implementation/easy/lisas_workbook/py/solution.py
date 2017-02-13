def solution(chapters, k):
    count = 0
    page  = 0

    for probCount in chapters:    
        for problem in range(1, 1 + probCount):
            if (problem - 1) % k == 0:
                page += 1
                
            if problem == page:
                count += 1
                
    return count

n, k  = map(int, input().split())
t     = map(int, input().split())
count = solution(t, k)

print(count)
