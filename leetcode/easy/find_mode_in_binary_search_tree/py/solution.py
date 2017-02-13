# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        
        if root == None:
            return []
            
        stack  = [root]
        lookup = collections.defaultdict(int)
        
        while len(stack) > 0:
            node = stack.pop()
            
            lookup[node.val] += 1
            
            if node.left != None:
                stack.append(node.left)
                
            if node.right != None:
                stack.append(node.right)
                
        maxCount = max(lookup.values())
        
        return [value for value in lookup if lookup[value] == maxCount]
