/*
 * The classic slow/fast pointer/index technique has its five minutes of fame again.
 * Have the fast pointer/index traverse the elements in the array, copying those,
 * which are not equal to the target value to the memory pointed to by the slow
 * pointer/index.
 *
 */

int removeElement(int* nums, int numsSize, int val) 
{
    int slow = 0;
    int fast = 0;
    
    while (fast < numsSize) {
        if (nums[fast] != val) {
            nums[slow] = nums[fast];
            ++slow;
        }
        ++fast;
    }
    
    return slow;
}
