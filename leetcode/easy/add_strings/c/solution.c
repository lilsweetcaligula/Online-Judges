#include <string.h>
#include <stdlib.h>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

char* addStrings(char* left, char* right)
{
    const int    BASE        = 10;
    const size_t leftCount   = strlen(left);
    const size_t rightCount  = strlen(right);
    const size_t resultCount = 1 + MAX(leftCount, rightCount);
    
    char *buffer = (char*)calloc(1 + resultCount, sizeof(*buffer));
    
    if (buffer)
    {
        const char *pleft  = &left[leftCount];
        const char *pright = &right[rightCount];
        
        char *presult = buffer;
        int   carry   = 0;
        
        while (1)
        {
            const int leftDigit  = pleft  > left  ? *--pleft  - '0' : 0;
            const int rightDigit = pright > right ? *--pright - '0' : 0;
            const int total      = carry + leftDigit + rightDigit;
            
            carry    = total / BASE;
            *presult = "0123456789"[total % BASE];
            
            ++presult;
            
            if (pleft == left && pright == right) {
                break;
            }
        }
        
        if (carry) {
            *presult++ = "0123456789"[carry];
        }
        
        *presult = '\0';
        
        for (char *begin = buffer, *end = presult; begin < end--; ++begin) 
        {
            const char temp = *begin;
            
            *begin = *end;
            *end   = temp;
        }
    }
    
    return buffer;
}
