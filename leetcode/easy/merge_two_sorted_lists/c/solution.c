/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) 
{
    struct ListNode 
        dummy = { .next = NULL },
        *dest = &dummy;
        
    while (l1 != NULL || l2 != NULL)
    {
        if (l1 == NULL) {
            dest->next = l2;
            l2 = l2->next;
        } else if (l2 == NULL) { 
            dest->next = l1;
            l1 = l1->next;
        } else if (l1->val < l2->val) {
            dest->next = l1;
            l1 = l1->next;
        } else {
            dest->next = l2;
            l2 = l2->next;
        }
        
        dest = dest->next;
    }
    
    return dummy.next;
}
