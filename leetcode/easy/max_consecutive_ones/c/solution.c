int findMaxConsecutiveOnes(int* nums, int numsSize) 
{
    int index    = 0;
    int count    = 0;
    int maxcount = 0;
    
    for (int index = 0; index <= numsSize; ++index) {
        if (index != numsSize && nums[index] == 1) {
            ++count;
        } else {
            maxcount = count > maxcount ? count : maxcount;
            count = 0;
        }
    }
    
    return maxcount;
}
