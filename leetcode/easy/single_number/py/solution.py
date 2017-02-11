#
# The functional approach we could use to locate the single number is
# to group the numbers by value and return the group with only a single 
# number in it.
#
# The caveat to the groupping approach is we need a sorted array for
# best performance - O(n log n). Hence: itertools.groupby(sorted(nums))
#
# A more costly alternative would be to use the key predicate taken
# by the itertools.groupby function, which gets the number's count
# via the list.count method. The time complexity of list.count method
# is O(n). When applied to n numbers, the overall solution complexity
# results in the unacceptable O(n^2).
#

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        # https://docs.python.org/3/library/itertools.html
        
        for num, group in itertools.groupby(sorted(nums)):
            count = len(tuple(group))
            
            if count == 1:
                return num
                
        return None
    
