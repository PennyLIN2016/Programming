class Solution:
    #Runtime: 1636 ms, faster than 28.25% of Python3 online submissions for Coin Change.
    #Memory Usage: 13.1 MB, less than 93.64% of Python3 online submissions for Coin Change.
    # dp solution: time o(n*m) time o(n)
    def coinChange(self, coins,amount):
        if not coins or amount<=0: return -1
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for value in coins:
            for i in range(value,amount+1):
                if dp[i-value]!=float('inf'):
                    dp[i]= min(dp[i],dp[i-value]+1)
        return -1 if dp[amount]==float('inf') else dp[amount]


if __name__ == '__main__':
    k = Solution()
    s= [1, 2, 5]
    j = 11

    r = k.coinChange(s,j)

    print(r)
    print('---End---')



