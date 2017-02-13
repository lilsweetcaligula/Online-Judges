# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root, depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return depth
            
        if root.left == None and root.right == None:
            return 1 + depth
            
        if root.left != None and root.right != None:
            return min(self.minDepth(root.left, 1 + depth), self.minDepth(root.right, 1 + depth))
            
        if root.left != None:
            return self.minDepth(root.left, 1 + depth)
            
        if root.right != None:
            return self.minDepth(root.right, 1 + depth)
            
        return depth
