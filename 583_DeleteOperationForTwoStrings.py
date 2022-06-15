class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Runtime: 232 ms, faster than 90.25% of Python online submissions for Delete Operation for Two Strings.
        # Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Delete Operation for Two Strings.
        # google solution : time o(n*m) space :o(n*m)
        return len(word1)+len(word2)-2*self.LenLCS(word1,word2)
    def LenLCS(self,s1,s2):
        n1, n2 = len(s1), len(s2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
###### python 3 solution
    def minDistance(self, word1: str, word2: str) -> int:
        # LCS question: find the longest common serial and the answer = l - lcs
        # dp solution
        # Runtime: 367 ms, faster than 58.35% of Python3 online submissions for Delete Operation for Two Strings.
        # Memory Usage: 16.1 MB, less than 63.70% of Python3 online submissions for Delete Operation for Two Strings.
        # time: o(m*n) space: o(n*m)
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # dp[i][j]: the lcs of s1[:i+1] of s2[:j+1]
        # two pos for two strings
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #dp[m][n] LCS
        return n + m - 2 * dp[m][n]

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 ="sea"
    n2= "eat"

    print('---Start---')
    print (n1)
    r = object.minDistance(n1,n2)
    print(r)
    print('---End---')
