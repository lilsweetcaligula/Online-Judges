#include <limits.h>

int findComplement(int num)
{
    unsigned result = 0;
    
    for (unsigned bit = 1; (bit & INT_MAX) && (bit <= num); bit <<= 1) {
        if (!(num & bit)) {
            result |= bit;
        }
    }
    
    return (int)result;
}
