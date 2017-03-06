/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/remove-nth-node-from-end-of-list
@Language: C++
@Datetime: 17-02-16 00:05
*/

/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: The head of linked list.
     */
    ListNode *removeNthFromEnd(ListNode *head, int n) 
    {
        auto dummy = ListNode{ 0 };
        dummy.next = head;
        
        auto slow  = &dummy;
        auto fast  = &dummy;
        
        while (n-- > 0) {
            fast = fast->next;
        }
        
        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        
        auto next = slow->next->next;
        delete slow->next; slow->next = next;
        
        return dummy.next;
    }
};
