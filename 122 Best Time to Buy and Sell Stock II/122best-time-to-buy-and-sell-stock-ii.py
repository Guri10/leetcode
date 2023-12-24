class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        profit=0
        for j in range(1,len(prices)):
            if prices[i]<prices[j]:
                profit += prices[j]-prices[i]
            i=j
        return profit