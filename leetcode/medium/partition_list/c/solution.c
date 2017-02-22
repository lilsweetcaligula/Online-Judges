/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) 
{
    struct ListNode left  = { 0 },
                    right = { 0 };

    struct ListNode *lnode = &left,
                    *rnode = &right,
                    *curr  = head;
                    
    while (curr != NULL) 
    {
        if (curr->val < x) {
            lnode->next = curr;
            lnode       = lnode->next;
        } else {
            rnode->next = curr;
            rnode       = rnode->next;
        }
        
        curr = curr->next;
    }
    
    lnode->next = right.next;
    rnode->next = NULL;
    
    return left.next;
}
