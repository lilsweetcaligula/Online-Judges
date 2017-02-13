# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        
        if root == None:
            return []
        
        result = []
        queue  = collections.deque((root,))
        
        while len(queue) > 0:
            level = []
            
            while len(queue) > 0:
                node = queue.popleft()
                level.append(node)
                
            result.append([node.val for node in level])
            
            for node in level:
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                    
        return result
            
