class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxp = 0
        while right < len(prices) :
            # p = prices[right] - prices[left]
            if prices[right] > prices[left]:
                maxp = max(prices[right] - prices[left],maxp)
            else:
                left = right
            right +=1
        return maxp
                