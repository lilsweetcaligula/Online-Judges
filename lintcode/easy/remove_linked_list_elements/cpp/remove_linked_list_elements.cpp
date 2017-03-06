/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/remove-linked-list-elements
@Language: C++
@Datetime: 17-02-15 20:08
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head a ListNode
     * @param val an integer
     * @return a ListNode
     */
    ListNode *removeElements(ListNode *head, int val) 
    {
        ListNode 
            dummy{ 0, head },
            *slow{ &dummy },
            *fast{ dummy.next };
            
        while (fast != nullptr) 
        {
            if (fast->val != val) {
                slow->next = fast;
                slow       = slow->next;
            }
            
            fast = fast->next;
        }
        
        slow->next = nullptr;
        
        return dummy.next;
    }
};