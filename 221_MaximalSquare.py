class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Runtime: 446 ms, faster than 85.29% of Python online submissions for Maximal Square.
        # Memory Usage: 33.1 MB, less than 23.03% of Python online submissions for Maximal Square.
        # dp solution dp[i][j]: i,j the right-bottom position: the max side of valid square
        # time: o(m*n) space: o(n*m)
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, m):
            for j in range(1, n):
                # if matrix[i][j] == 0, the position can be included in a valid square value = 0
                if int(matrix[i][j]) == 1:
                    # as a square, the three parts should be all 1
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return max(map(max, dp)) ** 2

obj = Solution()
t1 =  [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalSquare(t1))
print(t1)