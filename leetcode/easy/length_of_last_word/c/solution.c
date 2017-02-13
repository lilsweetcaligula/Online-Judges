#include <stdbool.h>
#include <string.h>
#include <ctype.h>

int lengthOfLastWord(char* s) 
{
    const char *end = &s[strlen(s)];
    int count       = 0;
    
    if (!*s) {
        return 0;
    }
    
    while (end > s && isspace(*--end)) {
        continue;
    }
    
    while (true) 
    {
        if (!isspace(*end)) {
            ++count;
        } else {
            break;   
        }
        
        if (end == s) {
            break;
        } else {
            --end;   
        }
    }
    
    return count;
}
