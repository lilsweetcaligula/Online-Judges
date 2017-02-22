# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        oddNodes  = []
        evenNodes = []
            
        node      = head
            
        while node != None:
            oddNodes.append(node)
            node = node.next
                
            if node != None:
                evenNodes.append(node)
                node = node.next
                    
        for i, node in enumerate(oddNodes):
            node.next = oddNodes[i + 1] if i + 1 < len(oddNodes) else None
            
        for i, node in enumerate(evenNodes):
            node.next = evenNodes[i + 1] if i + 1 < len(evenNodes) else None
                
        oddNodes[-1].next = evenNodes[0] if len(evenNodes) > 0 else None
    
        return oddNodes[0]
