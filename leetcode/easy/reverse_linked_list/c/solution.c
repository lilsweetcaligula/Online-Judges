/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) 
{
    if (head == NULL) {
        return NULL;    
    }
    
    struct ListNode 
        *node = head,
        *prev = NULL,
        *temp = NULL;
        
    while (node->next != NULL) {
        temp       = node->next;
        node->next = prev;
        prev       = node;
        node       = temp;
    }
    
    node->next = prev;
    
    return node;
}
