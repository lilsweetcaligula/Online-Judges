/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) 
{
    if (head == NULL) {
        return NULL;
    }
    
    struct ListNode oddGroup  = { 0 },
                    evenGroup = { 0 },
                    *oddNode  = &oddGroup,
                    *evenNode = &evenGroup,
                    *curr	  = head;
                    
    int i = 1;
    
    while (curr != NULL)
    {
        if (i % 2) {
            oddNode->next  = curr;
            oddNode        = oddNode->next;
        } else {
            evenNode->next = curr;
            evenNode       = evenNode->next;
        }
        
        curr = curr->next;
        ++i;
    }
    
    evenNode->next = NULL;
    oddNode->next  = evenGroup.next;
    
    return oddGroup.next;
}
