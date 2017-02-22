/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) 
{
    if (headA == NULL) {
        return NULL;
    }
    
    if (headB == NULL) {
        return NULL;
    }
    
    struct ListNode *tail = headA;
    
    while (tail->next != NULL) {
        tail = tail->next;
    }
    
    tail->next = headA;
    
    struct ListNode *slow = headB,
                    *fast = headB;
                    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            break;
        }
    }
    
    if (fast != NULL && fast->next != NULL) 
    {
        slow = headB;
                        
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        
        tail->next = NULL;
        
        return slow;
    }
    
    tail->next = NULL;
    
    return NULL;
}
