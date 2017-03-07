class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        if root == None:
            return None
            
        stack  = [root]
        curmax = root
        
        while len(stack) > 0:
            node   = stack.pop()
            curmax = max([node, curmax], key=lambda x: x.val)
            
            if node.left != None:
                stack.append(node.left)
                
            if node.right != None:
                stack.append(node.right)
                
        return curmax
