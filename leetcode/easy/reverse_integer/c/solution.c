#include <stdlib.h>
#include <limits.h>

int reverse(int x) 
{
    const int sign = x >= 0 ? 1 : -1;
    long long num  = abs(x);
    long long rev  = 0;
          
    while (num > 0) 
    {
        rev  = 10 * rev + num % 10;
        num /= 10;
    }
    
    if (rev < INT_MIN || rev > INT_MAX) {
        return 0;
    }
    
    return sign * (int)rev;
}
