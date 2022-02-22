class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dynamic programming solution: time: o(n*m) spcae: o(n)
        sortedCoins= sorted(coins)
        # dp[i]: how many coins sum up to i
        # float('inf')  means no solution
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in sortedCoins:
            if coin > amount:
                break
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]== float('inf') else dp[amount]







if __name__ == '__main__':
    k = Solution()
    s= [1, 2, 5]
    j = 11

    r = k.coinChange(s,j)

    print(r)
    print('---End---')
