/*
 * The good ol'slow/fast pointer/index approach coupled with the dummy
 * technique for linked lists. Simply allocate a dummy (preferrably on
 * the stack) and append all nodes which do not contain the target value
 * to it. At the end of the traversal, the next pointer of the dummy node
 * will be pointing to the new head.
 *
 * O(n) time, O(1) space.
 */

#include <stddef.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) 
{
    struct ListNode
        dummy = { .next = head },
        *slow = &dummy,
        *fast = &dummy;
        
    while (fast != NULL) {
        if (fast->next != NULL && fast->next->val == val) {
            fast = fast->next;   
        } else {
            slow->next = fast->next;
            fast = fast->next;
            slow = slow->next;
        }
    }
    
    return dummy.next;
}
