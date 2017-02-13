class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """        
        self._sums = [0]
        total      = 0
        
        for num in nums:
            total += num            
            self._sums.append(total)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sums[j + 1] - self._sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
