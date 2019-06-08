class Solution(object):
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # directly recursion solution Time Limit Exceeded
        res,i= n,2
        while(i*i<=n):
            k = int(n/(i*i))
            next = n % (i*i)
            res= min(res,k+self.numSquares(next))
            i+=1
        return res

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 4096 ms, faster than 32.02% of Python online submissions for Perfect Squares.
        #Memory Usage: 12 MB, less than 53.35% of Python online submissions for Perfect Squares.
        # dp[i] store the answer for i
        # time: O(nlgn) space : O(n)
        dp=[float('inf')]* (n+1)
        dp[0]=0
        for i in range(1,n+1):
            j=1
            while j*j<=i:
                # get min value in all possible answers.
                # dp[i] current possible min value for number i
                #dp[i-j*j]+1 the new solution value.
                dp[i]= min(dp[i],dp[i-j*j]+1)
                j+=1

        return dp[n]


if __name__ == '__main__':

    s= 68797

    object = Solution()
    r = object.numSquares(s)

    print(r)
    print('---End---')

