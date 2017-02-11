/*
 * The classic solution to check if an array contains a duplicate, is to sort
 * the array, thus groupping the duplicates, and traversing the sorted array,
 * looking ahead for duplicates. 
 *
 * It's important to point out that the loop omits the last element in the array,
 * - this is because if the last element in a sorted array has not had duplicates,
 * at this point, being the last element, it cannot have duplicates.
 */

#include <stdlib.h>

int compareIntegers(const int *lhs, const int *rhs) {
    return *lhs - *rhs;
}

bool containsDuplicate(int* nums, int numsSize) 
{
    qsort(nums, numsSize, sizeof(nums[0]), compareIntegers);
    
    for (int index = 0; index + 1 < numsSize; ++index) {
        if (nums[index] == nums[index + 1]) {
            return true;
        }
    }
    
    return false;
}
