# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        stack     = [root]
        depths    = [1]
        max_depth = 0
        
        while len(stack) > 0:
            
            node  = stack.pop()
            depth = depths.pop()
            
            max_depth = max(max_depth, depth)
            
            if node.left:
                stack.append(node.left)
                depths.append(depth + 1)
                
            if node.right:
                stack.append(node.right)
                depths.append(depth + 1)
        
        return max_depth
        
