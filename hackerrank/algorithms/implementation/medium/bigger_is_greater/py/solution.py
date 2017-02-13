def solution(s):
    #
    # The next permutation algorithm. For more information, please look up:
    # [href.] https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    # [href.] https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    #
    
    chars = list(s)
    i     = len(chars) - 1
    
    while i > 0 and chars[i - 1] >= chars[i]:
        i -= 1

    if i == 0:
        return None

    j = len(chars) - 1

    while chars[j] <= chars[i - 1]:
        j -= 1

    chars[i - 1], chars[j] = chars[j], chars[i - 1]

    return ''.join(chars[:i] + list(reversed(chars[i:])))
        
testCount = int(input())

for testId in range(testCount):
    word    = input().strip()    
    greater = solution(word)
    
    if greater:
        print(greater)
    else:
        print('no answer')
