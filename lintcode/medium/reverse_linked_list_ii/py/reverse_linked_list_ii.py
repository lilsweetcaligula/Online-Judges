"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        dummy      = ListNode(0)
        dummy.next = head
    
        prev  = None
        node  = dummy
        i     = 0
            
        while i < m:
            prev = node
            node = node.next
            i   += 1
                
        begin = prev
        end   = prev.next
        curr  = prev.next
            
        while i <= n and curr != None:
            temp      = curr.next
            curr.next = prev
            prev      = curr
            curr      = temp
            i        += 1
                
        begin.next = prev
        end.next   = curr
                
        return dummy.next
