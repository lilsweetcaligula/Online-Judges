# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, pathSum):
        """
        :type root:     TreeNode
        :type pathSum:  int
        :rtype:         bool
        """
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return pathSum - root.val == 0
        
        leftHasPathSum  = False
        rightHasPathSum = False
        
        if root.left != None:
            leftHasPathSum = self.hasPathSum(root.left,  pathSum - root.val) 
            
        if root.right != None:
            rightHasPathSum = self.hasPathSum(root.right, pathSum - root.val)
            
        return leftHasPathSum or rightHasPathSum
