/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/swap-nodes-in-pairs
@Language: C++
@Datetime: 17-02-16 00:56
*/

#include <stack>

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
     * @return a ListNode
     */
    ListNode* swapPairs(ListNode* head) 
    {
        auto stack = std::stack<ListNode*>{ };
        auto dummy = ListNode{ 0 };
        auto tail  = &dummy;
        auto curr  = head;
        
        while (curr != nullptr)
        {
            stack.push(curr);
            
            curr = curr->next;
            
            if (curr == nullptr || stack.size() == 2) 
            {
                while (stack.size() > 0) {
                    tail->next = stack.top();
                    tail       = tail->next;
                    stack.pop();
                }
                
                tail->next = nullptr;
            }
        }
        
        return dummy.next;
    }
};