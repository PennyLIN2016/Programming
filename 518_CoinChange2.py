class Solution(object):
    def change1(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # time out: 17 / 27 test cases passed.
        if amount<0: return 0
        if amount==0: return 1
        if not coins: return 0
        coins.sort()
        return self.dfs(amount,coins)
    def dfs(self,reminder,coin):
        print coin
        print('reminder:'+ str(reminder))
        p=len(coin)
        res=0
        while p>0:
            p-=1
            if coin[p]>reminder:
                continue
            if reminder%coin[p]==0:
                res+=1
                l=int(reminder/coin[p])
            else:
                l=int(reminder/coin[p])+1
            print ('dfs: 0 -  '+ str(int(reminder/coin[p])))
            print coin[:p]
            for n in range(1,l):
                if coin[:p]:
                    res+= self.dfs(reminder-coin[p]*n,coin[:p])
        return res
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Runtime: 164 ms, faster than 61.07% of Python online submissions for Coin Change 2.
        #Memory Usage: 11.8 MB, less than 66.67% of Python online submissions for Coin Change 2.
        # dp solution
        if amount<0:return 0
        dp = [0]*(amount+1)
        dp[0]=1
        for value in coins:
            for i in range(1,amount+1):
                if value<=i:
                    dp[i]+=dp[i-value]
        return dp[-1]

if __name__ == '__main__':
    object = Solution()
    A= 500
    c=[1,2,5]

    print('---Start---')
    print A
    r = object.change(A,c)
    #12701
    print(r)
    print('---End---')
