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