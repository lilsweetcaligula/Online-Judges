class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        lookup = { num: ind for ind, num in enumerate(numbers) }
        
        for ind, num in enumerate(numbers):
            if (target - num) in lookup:
                return [1 + ind, 1 + lookup[target - num]]
                
        return [-1, -1]
