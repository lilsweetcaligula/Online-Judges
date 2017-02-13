#include <string.h>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

char* addBinary(char* left, char* right)
{
    const char   BASE        = 2;
    const size_t leftCount   = strlen(left);
    const size_t rightCount  = strlen(right);
    const size_t resultCount = 1 + MAX(leftCount, rightCount);
    
    char *buffer = (char*)calloc(1 + resultCount, sizeof(*buffer));
    
    if (buffer) 
    {
        const char *pleft   = &left[leftCount];
        const char *pright  = &right[rightCount];
        
        char *presult = buffer;
        int   carry   = 0;
        
        while (1)
        {
            const int leftBit  = pleft  > left  ? *--pleft  - '0' : 0;
            const int rightBit = pright > right ? *--pright - '0' : 0;
            const int total    = carry + leftBit + rightBit;
            
            carry    = total / BASE;
            *presult = "01"[total % BASE];
            
            ++presult;
            
            if (pleft == left && pright == right) {
                break;
            }
        }
        
        if (carry) {
            *presult++ = "01"[carry];
        }
        
        *presult = '\0';
        
        for (char *begin = buffer, *end = presult; begin < end--; ++begin) {
            const char temp = *begin;
            
            *begin = *end;
            *end   = temp;
        }
    }
    
    return buffer;
}
