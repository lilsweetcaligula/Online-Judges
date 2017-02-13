def solution(nums):
    import collections
    
    if len(nums) == 0:
        return 0
    
    item, count = collections.Counter(nums).most_common()[0]
    
    return len(nums) - count

n    = int(input())
nums = tuple(map(int, input().split()))

cnt  = solution(nums)

print(cnt)
