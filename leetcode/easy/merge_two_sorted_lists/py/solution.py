# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dest  = dummy
        
        node1 = l1
        node2 = l2
        
        while node1 != None and node2 != None:
            
            if node1.val < node2.val:
                dest.next = node1
                node1     = node1.next
            else:
                dest.next = node2
                node2     = node2.next
                
            dest = dest.next
            
        while node1 != None:
            dest.next = node1
            dest      = dest.next
            node1     = node1.next
            
        while node2 != None:
            dest.next = node2
            dest      = dest.next
            node2     = node2.next
            
        return dummy.next
