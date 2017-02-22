# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
    
        stack = [root]
        dummy = TreeNode(0)
        tail  = dummy
    
        while len(stack) > 0:
            node       = stack.pop()
            tail.right = node
            tail       = tail.right
    
            if node.right != None:
                stack.append(node.right)
    
            if node.left != None:
                stack.append(node.left)
    
        tail.right = None
        node       = dummy
        
        while node != None:
            node.left = None
            node      = node.right
    
        root = dummy.right
            
