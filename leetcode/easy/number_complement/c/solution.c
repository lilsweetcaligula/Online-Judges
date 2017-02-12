#include <limits.h>

int findComplement(int num)
{
    unsigned mask = 0;
    unsigned bit  = 1;
    
    while (bit <= (unsigned)num) {
        mask  = (mask << 1) | 1;
        bit <<= 1;
    }
    
    return (~num) & mask;
}
