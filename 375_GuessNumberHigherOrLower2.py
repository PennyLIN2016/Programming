class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 460 ms, faster than 83.59% of Python online submissions for Guess Number Higher or Lower II.
        #Memory Usage: 12.3 MB, less than 56.41% of Python online submissions for Guess Number Higher or Lower II.
        # time(n**3) space:o(n**2)
        # mix(max) solution:
        # dp[i][j]: the min(max) between i and j
        dp =[[0]*(n+1) for _ in range(n+1)]
        # i [n-1,1]
        for i in range(n-1,0,-1):
            for j in range(i+1,n+1):
                #  travel all possible x in [i,j]
                # for a value = x ,cost =  value + max(dp[i][value-1],dp[value+1][j]) the worest case for this value.
                # for dp[i][j]  get the the min cost for all possible cost in [i][j]
                # so make sure to get the min(min) cost to guarantee a win(max).
                dp[i][j]=min(value+max(dp[i][value-1],dp[value+1][j]) for value in range(i,j))
        return dp[1][n]



if __name__ == '__main__':
    object = Solution()
    k = 10


    r = object.getMoneyAmount(k)
    print(r)
    print('---End---')
