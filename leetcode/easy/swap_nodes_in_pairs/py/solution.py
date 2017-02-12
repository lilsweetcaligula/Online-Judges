#
# Another approach to solve the problem still makes use
# of the dummy node technique, however this time around
# we do not actually append to the "dummy"-headed list's
# tail. Instead we use the dummy to accommodate the "prev"
# pointer on the first iteration of the loop. The "prev"
# pointer points to the last node of the previous swapped
# pair.
#
# When the traversal's done, the next pointer of the dummy
# node will be pointing to the new head of the list (the
# second node of the original list).
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
    
        dummy      = ListNode(0)
        dummy.next = head
    
        first      = head
        second     = head.next
        prev       = dummy
    
        while first != None and second != None:
            nextPair    = second.next
            first.next  = nextPair
            second.next = first
    
            prev.next   = second
            prev        = first
    
            first       = nextPair
    
            if nextPair != None:
                second = nextPair.next
    
        return dummy.next
