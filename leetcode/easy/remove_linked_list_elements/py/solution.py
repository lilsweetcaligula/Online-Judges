# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy      = ListNode(0)
        dummy.next = head
        
        slow       = dummy
        fast       = dummy
        
        while fast.next != None:
            if fast.next.val != val:
                slow.next = fast.next
                slow      = slow.next
            fast = fast.next
        slow.next = None
            
        return dummy.next
