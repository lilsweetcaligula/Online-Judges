# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head  = head
        self.count = 0
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            self.count += 1
            
            slow = slow.next
            fast = fast.next.next
        else:
            self.count *= 2
            
            if fast != None:
                self.count += 1
                
        self.mid = slow
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        
        import random
        
        rand = random.randint(0, self.count - 1)
                
        if rand < self.count // 2:
            begin = 0
            node  = self.head
        else:
            begin = self.count // 2
            node  = self.mid
            
        for _ in xrange(begin, rand):
            node = node.next
            
        return node.val
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
