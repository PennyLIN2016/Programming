class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)< 2:
            return 0
        high, low = prices[0],prices[0]
        profit = 0
        flag = 0
        for i in xrange(0,len(prices)):
            if flag == 0:
                if low > prices[i]:
                    high, low = prices[i],prices[i]
                else:
                    high = prices[i]
                    flag = 1
                continue
            if flag == 1:
                if high <= prices[i]:
                    high = prices[i]
                else:
                    profit += (high -low)
                    high, low = prices[i],prices[i]
                    flag = 0
        if flag == 1:
            return profit + (high -low)
        else:
            return profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)< 2:
            return 0
        profit = 0
        for i in xrange(1,len(prices)):
            if prices[i]-prices[i-1]> 0:
                profit += prices[i]-prices[i-1]
        return profit




if __name__ == '__main__':

    inputs = [7, 1, 5, 3, 6, 4]

    #inputs = [2,4]
    #inputs =[3,2,6,5,0,3]
    #inputs= [1,4,1,4,3,1]

    k = Solution()
    r = k.maxProfit2(inputs)

    print r
