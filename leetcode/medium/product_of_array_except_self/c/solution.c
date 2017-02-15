#include <stdlib.h>
#include <string.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize)
{
   /*
    * The function does not alter the size of the parameter array,
    * however, we defer the assignment of the array size until
    * the very end, just in case something goes wrong. If it does,
    * the caller should receive the array size as 0.
    */
    *returnSize = 0;

    int *leftprods = (int*)malloc(sizeof(*leftprods) * numsSize);
    
    if (leftprods) 
    {
        int *rightprods = (int*)malloc(sizeof(*rightprods) * numsSize);

        if (rightprods)
        {
            int *result = (int*)malloc(sizeof(*result) * numsSize);

            if (result) 
            {
               /* 
	        * Accumulate products from left to right. Since we are not
	        * allowed to use division, we store accumulated products
	        * to the left of the current value in one array, and to the
	        * right in another one.
	        */            
                for (int index = 0, product = 1; index < numsSize; ++index) {
                    product         *= nums[index];
                    leftprods[index] = product;                    
                }

               /*
                * Accumulate products from right to left.
                */
                for (int index = 0, product = 1; index < numsSize; ++index) {
                    product                         *= nums[numsSize - index - 1];
                    rightprods[numsSize - index - 1] = product;
                }

               /*
                * Compute the result. The general idea is to multiply
                * the accumulated product to the left of the current
                * value by the accumulated product of the values to
                * the right of it.
                */
                for (int index = 0; index < numsSize; ++index) {
                    result[index] = 
                        (index > 0 ? leftprods[index - 1] : 1) 
                        * (index + 1 < numsSize ? rightprods[index + 1] : 1);
                }

               /*
	        * The function does not alter the size of the parameter array,
	        * since everything went smooth, simply assign numsSize to the
	        * memory pointed to by the returnSize pointer.
	        */
                *returnSize = numsSize;

                free(leftprods);  leftprods  = NULL;
                free(rightprods); rightprods = NULL;

                return result;
            } else {
                free(leftprods);  leftprods  = NULL;
                free(rightprods); rightprods = NULL;

                return NULL;
            }
        } else {
            free(leftprods); leftprods = NULL;

            return NULL;
        }
    }

    return NULL;
}
