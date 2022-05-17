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
    
    class Solution:
    def longestPalindromeSubseq1(self, s: str) -> int:
        # timeout: 61 / 86 test cases passed.
        # force recursion solution
        def getLongest(i, j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return getLongest(i+1, j-1) + 2
            return max(getLongest(i+1, j), getLongest(i, j-1))
        return getLongest(0, len(s)-1)

    def longestPalindromeSubseq(self, s: str) -> int:
        # Runtime: 1417 ms, faster than 80.40% of Python3 online submissions for Longest Palindromic Subsequence.
        # Memory Usage: 30.7 MB, less than 64.24% of Python3 online submissions for Longest Palindromic Subsequence.
        # dp solution: time: o(n**2) space: o(n**2)
        l = len(s)
        # dp[i][j]: the longest subseq lenght of sub s[i:j+1]
        dp = [[0] * l for _ in range(l)]
        #
        for i in range(l-1, -1,-1):
            dp[i][i] = 1
            for j in range(i+1, l):
                if s[i] == s[j]:
                    # the longest subseq can extend two chars.
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # skip one of the two chars
                    # the recursion relationship have to travel the i from the end.
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][l-1]



if __name__ == '__main__':
    object = Solution()
    A= "bbbab"

    print('---Start---')
    print A
    r = object.longestPalindromeSubseq(A)
    print(r)
    print('---End---')
