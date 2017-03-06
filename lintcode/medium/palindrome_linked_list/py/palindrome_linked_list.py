# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        if head == None:
            return True
            
        prev = None
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        mid  = slow
        curr = mid
        
        while curr != None:
            temp      = curr.next
            curr.next = prev
            prev      = curr
            curr      = temp
            
        left  = head
        right = prev
        
        while left != mid:
            if left.val != right.val:
                return False
                
            left  = left.next
            right = right.next
            
        return True
