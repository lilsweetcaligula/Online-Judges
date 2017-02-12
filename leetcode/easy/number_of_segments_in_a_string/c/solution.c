/*
 * A purely procedural solution to the problem involves traversing
 * the string and incrementing the counter by one each time we 
 * encounter the end of the current segment.
 */

#include <ctype.h>

int countSegments(char* s) 
{
    int count = 0;
    
    while (*s)
    {
        while (isspace(*s)) ++s;
        
        if (*s) {
            ++count;
            while (*s && !isspace(*s)) ++s;
        }
    }
    
    return count;
}
