/*
 * In order to solve the single number problem, we need to calculate the number
 * of times each number appears in the array. While we could loop the array for
 * each number, this will result in the O(n^2) performance. Arguably, the smarter
 * way would be to sort the array, which will enable us to calculate the frequency
 * of each number in O(n) time.
 */

#include <stdlib.h>

int compareIntegers(const int *lhs, const int *rhs) {
    return *lhs - *rhs;
}

int singleNumber(int* nums, int numsSize) {
    if (numsSize > 1) {
        // Sort the array to enable frequency counting in O(n) time.
        qsort(nums, numsSize, sizeof(nums[0]), compareIntegers);        
        
        for (int index = 1, count = 1; index < numsSize; ++count, ++index) {
            // Is this a duplicate of the previous value?
            if (nums[index] != nums[index - 1]) {
                // If it's not a duplicate, is it single?
                if (count == 1) {
                    return nums[index - 1];
                }
                count = 0;
            }
        }
        
        return nums[numsSize - 1];
    } else if (numsSize == 1) {
        return nums[0];
    }
    return 0;
}
