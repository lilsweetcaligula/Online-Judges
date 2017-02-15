#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <tgmath.h>

char *intToString(int value, char *buffer)
{
    static const char *DIGITS = "0123456789";
    char *pdig = buffer;

    while (value != 0) {
        *pdig++ = DIGITS[abs(value % 10)];
        value  /= 10;
    }
    
    *pdig = '\0';
    
    for (char *begin = buffer, *end = pdig; begin < end--; ++begin) {
        const char temp = *begin;
        *begin = *end;
        *end   = temp;
    }
    
    return buffer;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) 
{
    /* Do not move these strings from the stack!!!
     * We depend on them being on the stack to
     * extract their size in O(1) via sizeof operator.
     */
    static const char FIZZ_BUZZ[] = "FizzBuzz";
    static const char FIZZ[]      = "Fizz";
    static const char BUZZ[]      = "Buzz";
    
    *returnSize = 0;
    
    char **result = (char**)malloc(sizeof(*result) * n);
    
    if (result) 
    {
        *returnSize = n;
        
        for (int index = 0, value = 1; index < n; ++index, ++value)
        {
            char *entry = NULL;
            
            if (value % 15 == 0) {
                entry = (char*)malloc(1 + sizeof(*entry) * sizeof(FIZZ_BUZZ)/sizeof(FIZZ_BUZZ[0]));
                
                if (entry) {
                    (void)strcpy(entry, FIZZ_BUZZ);
                }
            } else if (value % 5 == 0) {
                entry = (char*)malloc(1 + sizeof(*entry) * sizeof(BUZZ)/sizeof(BUZZ[0]));
                
                if (entry) {
                    (void)strcpy(entry, BUZZ);
                }
            } else if (value % 3 == 0) {
                entry = (char*)malloc(1 + sizeof(*entry) * sizeof(FIZZ)/sizeof(FIZZ[0]));
                
                if (entry) {
                    (void)strcpy(entry, FIZZ);
                }
            } else {
                entry = (char*)malloc(1 + sizeof(*entry) * (1 + log10(INT_MAX)));
                
                if (entry) {
                    (void)strcpy(entry, intToString(value, entry));
                }
            }
            
            if (!entry)
            {
                for (int j = 0; j < index; ++j) {
                    free(result[j]); result[j] = NULL;
                }
                
                return NULL;
            } else {
                result[index] = entry;
            }
        }
    }
    
    return result;
}
