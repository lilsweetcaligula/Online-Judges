#include <stdint.h>

uint32_t reverseBits(uint32_t n) 
{
    uint32_t result   = 0;    
    uint32_t src_bit  = 1;
    uint32_t dest_bit = 1 << (sizeof(n) * 8 - 1);
    
    while (dest_bit > 0) 
    {    
        if (n & src_bit) {
            result |= dest_bit;
        }
        
        dest_bit >>= 1; 
        src_bit  <<= 1;
    }
    
    return result;
}
