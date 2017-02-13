# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findMiddle(self, head):
        """
        :type head: ListNode
        :rtype:     ListNode
        """
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reverse(self, head):
        """
        :type head: ListNode
        :rtype:     ListNode
        """
        prev = None
        curr = head
        
        while curr != None:
            temp      = curr.next
            curr.next = prev
            prev      = curr
            curr      = temp
            
        return prev
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype:     bool
        """
        mid   = self.findMiddle(head)
        left  = head
        right = self.reverse(mid)
        
        while left != mid:
            if left.val != right.val:
                return False
            else:
                left  = left.next
                right = right.next
            
        return True
