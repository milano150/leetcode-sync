class Solution(object):
    def maxProfit(self, prices):

        h = 0
        t = 1
        profit = 0

        while t < len(prices):

            if prices[t] > prices[h]:
                p = prices[t] - prices[h]
                profit = max(profit, p)

            else:
                h = t

            t += 1

        return profit