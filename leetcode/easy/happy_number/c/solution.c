static int sumSquaredDigits(int n)
{
    int value = 0;
    
    while (n > 0) 
    {
        value += (n % 10) * (n % 10);
        n     /= 10;
    }
    
    return value;
}

bool isHappy(int n) 
{
    int slow = n;
    int fast = sumSquaredDigits(n);
    
    while (slow != 1 && fast != 1) 
    {
        if (fast == slow) {
            return false;
        }
        
        slow = sumSquaredDigits(slow);
        
        for (int times = 0; times < 2; ++times) 
        {
            fast = sumSquaredDigits(fast);
        }
    }
    
    return true;
}
