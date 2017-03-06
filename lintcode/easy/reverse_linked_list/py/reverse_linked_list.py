# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: Python
@Datetime: 17-02-16 00:10
'''

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr != None:
            temp      = curr.next
            curr.next = prev
            prev      = curr
            curr      = temp
            
        return prev