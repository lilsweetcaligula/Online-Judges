class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node 
    def maxNode(self, root):
        def helper(root, curmax):
            if root == None:
                return curmax
                
            curmax = max([root, curmax], key=lambda x: x.val)
            
            return max(
                curmax, 
                helper(root.left, curmax), 
                helper(root.right, curmax),
                key=lambda x: x.val)
            
        if root == None:
            return None
        
        return helper(root, root)
