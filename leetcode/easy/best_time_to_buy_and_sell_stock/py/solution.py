class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lookup = sorted(range(len(prices)), reverse=True, key=lambda x: prices[x])
        i = j = 0
        max_profit = 0
    
        while i < len(prices):
            max_profit = max(max_profit, prices[lookup[j]] - prices[i])
            if i == lookup[j]:
                while j < len(lookup) and lookup[j] <= i:
                    j += 1
            i += 1
            
        return max_profit
