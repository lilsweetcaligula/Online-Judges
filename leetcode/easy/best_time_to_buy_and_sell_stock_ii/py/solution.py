class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i      = 0
    
        while i + 1 < len(prices):            
            j = i
            
            while j + 1 < len(prices) and prices[j + 1] > prices[j]:
                j += 1
                
            profit += prices[j] - prices[i]            
            i       = j + 1
            
        return profit
