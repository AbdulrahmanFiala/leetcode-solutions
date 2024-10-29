class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if (prices[i - 1] < prices[i]):
                profit += (prices[i] - prices[i-1])
        return profit

# Explanation Video (https://www.youtube.com/watch?v=3SJ3pUkPQMc)