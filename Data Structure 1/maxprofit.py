class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curmin = prices[0]
        
        for i in range(1,len(prices)):
            curprofit = prices[i] - curmin
            
            if curprofit>max_profit:
                max_profit = curprofit
            
            if curmin>prices[i]:
                 curmin = prices[i]
                    
        return max_profit