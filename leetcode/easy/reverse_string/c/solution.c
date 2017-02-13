#include <string.h>

char* reverseString(char* s) 
{
    for (char *begin = s, *end = &s[strlen(s)]; begin < end--; ++begin) 
    {
        const char temp = *begin;
        
        *begin = *end;
        *end   = temp;
    }
    
    return s;
}
