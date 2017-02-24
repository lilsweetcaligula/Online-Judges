# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
            
        dummy      = ListNode(0)
        dummy.next = head        
        curr       = dummy
            
        for _ in range(m - 1):
            if curr == None:
                return dummy.next
            else:
                curr = curr.next
            
        prev  = curr
        start = curr
        end   = curr.next
        curr  = curr.next
    
        for _ in range(m, n + 1):
            if curr == None:
                break
            else:
                temp      = curr.next
                curr.next = prev
                prev      = curr
                curr      = temp
            
        start.next = prev
        end.next   = temp    
    
        return dummy.next
