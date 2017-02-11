#include <stdlib.h>

int compareIntegers(const int *lhs, const int *rhs) {
    return *lhs - *rhs;
}

int singleNumber(int* nums, int numsSize) {
    if (numsSize > 1) {
        qsort(nums, numsSize, sizeof(nums[0]), compareIntegers);
        
        for (int index = 1, count = 1; index < numsSize; ++count, ++index) {
            if (nums[index] != nums[index - 1]) {
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
