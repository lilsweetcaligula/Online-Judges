# Slow. Horrible. Ugly. Don't try this at home.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    @staticmethod
    def computeHeight(root, curHeight=0):
        if root == None:
            return curHeight
            
        return max(
            Solution.computeHeight(root.left,  1 + curHeight), 
            Solution.computeHeight(root.right, 1 + curHeight)
        )
    
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        if root == None:
            return True
            
        if abs(  Solution.computeHeight(root.left)
               - Solution.computeHeight(root.right)
               ) < 2:
                  
            return self.isBalanced(root.left) and self.isBalanced(root.right)
            
        return False
