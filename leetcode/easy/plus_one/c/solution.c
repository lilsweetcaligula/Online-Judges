#include <stdlib.h>
#include <string.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) 
{
    int *dest = (int*)malloc(sizeof(*dest) * (1 + digitsSize));
    
    if (dest)
    {
      int carry   = 0;
      *returnSize = 0;

      for (int index = digitsSize - 1; index >= 0; --index)
      {
        const int sum = digits[index] + carry;

        if (index == digitsSize - 1) sum += 1;

        dest[index] = sum % 10;
        carry       = sum / 10;

        ++*returnSize;
      }

      if (carry > 0) {
        dest[(*returnSize)++] = carry;

        for (int left = 0, right = *returnSize; left < right--; ++left) {
          const int temp = dest[left];

          dest[left]  = dest[right];
          dest[right] = temp;
        }
      }
    }
    
    return dest;
}
