import collections
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #Runtime: 2648 ms, faster than 70.80% of Python online submissions for Ones and Zeroes.
        #Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Ones and Zeroes.
        # dp solution: time:o(l*m*n) space:o(m*n)
        if not strs or m+n==0: return 0
        # dp[i][j]: the max str number of i zeros and j ones standing for.
        dp=[[0 for i in range(n+1)] for _ in range(m+1)]
        for v in strs:
            zeros,ones=0,0
            for c in v:
                if c=="0":zeros+=1
                elif c=="1":ones+=1
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)
        return dp[m][n]

        #Runtime: 3226 ms, faster than 76.52% of Python3 online submissions for Ones and Zeroes.
        #Memory Usage: 14.1 MB, less than 81.81% of Python3 online submissions for Ones and Zeroes.
        # greedy solution: time: o(l*m*n) space: (m*n)
        # for the i bit 0 and j bit 1 : max size of subset
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for v in strs:
            # count characters
            zeros, ones = 0, 0
            for char in v:
                if char == '0':
                    zeros += 1
                else:
                    ones += 1
            # ensure the i, j > zeros and ones
            # start from m, n to zeros and ones.
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    print(dp)
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]

if __name__ == '__main__':
    object = Solution()
    A= ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print('---Start---')
    r = object.findMaxForm(A,m,n)
    print(r)
    print('---End---')
