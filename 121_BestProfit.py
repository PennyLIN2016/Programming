class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        profit = 0
        for i in xrange(len(prices)-1):
            for j in xrange(i+1,len(prices)):
                profit = max((prices[j]-prices[i]),profit)

        return profit




if __name__ == '__main__':

    #inputs = [7, 1, 5, 3, 6, 4]

    #inputs = [2,4,1]
    #inputs =[3,2,6,5,0,3]
    inputs= [1,4,1,4,3,1]

    k = Solution()
    r = k.maxProfit(inputs)

    print r
