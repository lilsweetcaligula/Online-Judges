# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype:     TreeNode
        """
        
        def sortedArrayToBSTHelper(nums, lo, hi):
            """
            :type nums: List[int]
            :type lo:   int
            :type hi:   int
            :rtype:     TreeNode
            """
            if hi <= lo:
                return None
            
            mid  = lo + (hi - lo) // 2
            node = TreeNode(nums[mid])
            
            node.left  = sortedArrayToBSTHelper(nums, lo, mid)
            node.right = sortedArrayToBSTHelper(nums, mid + 1, hi)
            
            return node
            
        return sortedArrayToBSTHelper(nums, 0, len(nums))
