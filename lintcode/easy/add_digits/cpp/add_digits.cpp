class Solution {
public:
    /**
     * @param num a non-negative integer
     * @return one digit
     */
    int addDigits(int num) 
    {
        while (num > 9) 
        {
            decltype(num) next = 0;
            
            while (num > 0) {
                next += num % 10;
                num  /= 10;
            }
            
            num = next;
        }
        
        return num;
    }
};
