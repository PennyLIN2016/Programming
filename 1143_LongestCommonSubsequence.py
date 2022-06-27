class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Runtime: 508 ms, faster than 38.92% of Python online submissions for Longest Common Subsequence.
        # Memory Usage: 21.5 MB, less than 84.53% of Python online submissions for Longest Common Subsequence.
        # dp solution: time: o(l1*l2) space: o(l1*l2)
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            print(dp)
        return dp[-1][-1]


obj = Solution()
t1 = "abcde"
t2 = "ace"
print(obj.longestCommonSubsequence(t1, t2))
