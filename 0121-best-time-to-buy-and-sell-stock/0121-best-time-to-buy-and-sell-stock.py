class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # n = len(prices)
        # prices.reverse()
        # for i in range(n):   
        #     for j in range(i, n):
        #         profit = prices[i] - prices[j]
        #         if profit > max_profit:
        #             max_profit = profit           
        # return max_profit 

        n=len(prices)
        buy = 0
        sell = 1
        max_profit = 0
        while sell < n:
            profit = prices[sell] - prices[buy]
            if profit > 0:
                if max_profit < profit:
                    max_profit = profit
            else:
                buy = sell
            sell += 1
        return max_profit



        