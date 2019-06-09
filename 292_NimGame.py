class Solution(object):
    def canWinNim1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # time out
        if n <=3: return True
        dp=[True]*n
        dp[0]=dp[1]=dp[2]=True
        for i in range(3,n):
            if dp[i-1] and dp[i-2] and dp[i-3]:
                dp[i]= False
        return dp[n-1]
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Runtime: 16 ms, faster than 88.48% of Python online submissions for Nim Game.
        #Memory Usage: 11.7 MB, less than 73.93% of Python online submissions for Nim Game.
        #time o(1) space (constant)
        return n%4 != 0

if __name__ == '__main__':
    k = Solution()
    s = 5
    r = k.canWinNim(s)

    print(r)
    print('---End---')



