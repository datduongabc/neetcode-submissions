class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        if len(prices) < 2:
            return 0
        
        left, right = 0, 1
        max_profit = 0

        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if profit < 0:
                left = right
            right += 1

        return max_profit