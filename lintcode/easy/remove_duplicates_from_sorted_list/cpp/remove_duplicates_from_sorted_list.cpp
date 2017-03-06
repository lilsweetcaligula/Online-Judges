/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list
@Language: C++
@Datetime: 17-02-15 23:51
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
     * @return: head node
     */
    ListNode *deleteDuplicates(ListNode *head) 
    {
        if (head == nullptr) {
            return nullptr;
        }
        
        auto slow = head;
        auto fast = head->next;
        
        while (fast != nullptr) {
            if (slow->val != fast->val) {
                slow->next = fast;
                slow       = slow->next;
            }
            fast = fast->next;
        }
        
        slow->next = nullptr;
        
        return head;
    }
};