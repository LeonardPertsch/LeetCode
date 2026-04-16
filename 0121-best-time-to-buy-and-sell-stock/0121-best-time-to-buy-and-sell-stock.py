class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        lowest = prices[0]
        profit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = max(profit, price - lowest)

        return profit
