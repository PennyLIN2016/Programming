class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Runtime: 24 ms, faster than 84.35% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
        # Memory Usage: 11.9 MB, less than 64.97% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
        # time: O(N), space: O(1) dp solution.

        if not prices: return 0
        selling=0#if the i is in selling status. the max value.
        cool=0 #if the i is in cool status. the max value.
        #buying=float('-inf') the same to -prices[0]
        buying = -prices[0] #if the i is in buying status. the max value.
        for value in prices:
            pre_selling= selling
            # if the i is in selling status, the i-1 could be buying or cool. the max should be the previous max buying + the current price.
            selling= buying+value
            # if the i in buying status. the i-1 should be cool or buying.
            buying = max(cool-value,buying)
            # if the i is in cool status, the i-1 should be cool /buying/ selling. if the max should come from previous cool or selling status.
            cool = max(cool, pre_selling)
        # the last max status should be selling or cool.
        return max(cool,selling)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Runtime: 24 ms, faster than 84.35% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
        # Memory Usage: 11.9 MB, less than 74.33% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
        # time O(N) Space: O(N)
        if not prices or len(prices)<2:return 0
        dp_buy=[0]*len(prices)# save max value if the status is holding stock in i
        dp_sell=[0]*len(prices)# save max value if the status is holding stock in i
        dp_buy[0],dp_buy[1]= -prices[0],max(-prices[0],-prices[1])
        dp_sell[1] = max(0,prices[1]-prices[0]) # the max always >= 0
        for i in range(2,len(prices)):
            dp_buy[i]=max(dp_sell[i-2]-prices[i],dp_buy[i-1])
            dp_sell[i]= max(dp_buy[i-1]+prices[i],dp_sell[i-1])
        return dp_sell[-1]


if __name__ == '__main__':
    s=  [1,2,3,0,2]

    p = Solution()
    print(p.maxProfit(s))