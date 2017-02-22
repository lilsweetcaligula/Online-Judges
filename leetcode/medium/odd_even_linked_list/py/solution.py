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
        
        oddDummy  = ListNode(0)
        evenDummy = ListNode(0)
        
        oddNode   = oddDummy
        evenNode  = evenDummy
        
        curr      = head
        
        while curr != None:
            for parent, child in zip([oddNode, evenNode], [curr, curr.next]):
                parent.next = child
                
            oddNode  = oddNode.next   if oddNode   != None else None
            evenNode = evenNode.next  if evenNode  != None else None
            curr     = curr.next.next if curr.next != None else None
            
        oddNode.next = evenDummy.next
        
        return oddDummy.next
