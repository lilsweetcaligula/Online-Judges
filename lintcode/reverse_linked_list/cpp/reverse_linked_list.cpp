/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/reverse-linked-list
@Language: C++
@Datetime: 17-02-16 00:13
*/

/**
 * Definition of ListNode
 * 
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 * 
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
     * @return: The new head of reversed linked list.
     */
    ListNode *reverse(ListNode *head) 
    {
        ListNode *prev{ nullptr },
                 *curr{ head };
                  
        while (curr != nullptr) 
        {
            auto next  = curr->next;
            curr->next = prev;
            prev       = curr;
            curr       = next;
        }
        
        return prev;
    }
};
