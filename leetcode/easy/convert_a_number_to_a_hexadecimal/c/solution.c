#include <stdlib.h>
#include <string.h>

char* toHex(int num) 
{
    static const size_t  BUFFER_SIZE = 1 + 2 * sizeof(num);
    static const char   *HEX_LOOKUP  = "0123456789abcdef";
    static const int     BASE        = 16;
    
    unsigned  bits  = (unsigned)num;
    char     *hex   = (char*)malloc(sizeof(*hex) * BUFFER_SIZE);
    
    if (hex) 
    {
        char *pchar = hex;
        
        do {
            *pchar++  = HEX_LOOKUP[bits % BASE];
            bits     /= BASE;
        } while (bits > 0);
        
        *pchar = '\0';
        
        char *begin = hex;
        char *end   = pchar - 1; 
        
        while (begin < end) 
        {
            const char temp = *begin;
            
            *begin = *end;
            *end   =  temp;
            
            ++begin; --end;
        }
    }
    
    return hex;
}
