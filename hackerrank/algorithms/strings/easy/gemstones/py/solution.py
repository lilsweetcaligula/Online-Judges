def solution(rocks):
    elems = set(rocks[0])
    
    for index in range(1, len(rocks)):
        rock = set(rocks[index])
        
        for elem in tuple(elems):
            if elem not in rock:
                elems.remove(elem)
                
    return len(elems)

count = int(input())
rocks = tuple(input().strip() for i in range(count))

print(solution(rocks))
