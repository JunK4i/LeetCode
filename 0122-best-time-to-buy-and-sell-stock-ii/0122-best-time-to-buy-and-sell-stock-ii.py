class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Intuition is that if you think graphically, u sum up the profit of each day segment, you can get the max profits
        # Each day, consider if you can profit of buying from the previous day and selling today. (since you can buy and sell on each day)
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
            print(max(0, prices[i]-prices[i-1]))
        return profit