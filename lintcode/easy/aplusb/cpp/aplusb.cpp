class Solution {
public:
    /*
     * @param a: The first integer
     * @param b: The second integer
     * @return: The sum of a and b
     */
    int aplusb(int a, int b) 
    {
        auto sum   = a;
        auto carry = b;
        
        while (carry != 0) 
        {
            const auto newSum = sum ^ carry;
            
            carry = (sum & carry) << 1;
            sum   = newSum;
        }
        
        return sum;
    }
};
