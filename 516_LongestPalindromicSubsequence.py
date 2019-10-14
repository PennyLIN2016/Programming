class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Runtime: 1244 ms, faster than 74.67% of Python online submissions for Longest Palindromic Subsequence.
        #Memory Usage: 26.4 MB, less than 50.00% of Python online submissions for Longest Palindromic Subsequence.
        # dp solution

        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    # reslut of s[i..j]
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
                print dp
        return dp[0][-1]



if __name__ == '__main__':
    object = Solution()
    A= "bbbab"

    print('---Start---')
    print A
    r = object.longestPalindromeSubseq(A)
    print(r)
    print('---End---')
