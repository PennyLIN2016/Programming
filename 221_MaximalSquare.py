class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #Runtime: 172 ms, faster than 54.77% of Python online submissions for Maximal Square.
        #Memory Usage: 19.8 MB, less than 11.79% of Python online submissions for Maximal Square.
        if not matrix: return  0
        m = len(matrix)
        n = len(matrix[0])
        d = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    d[i][j]= int(matrix[i][j])
                else:
                    if int(matrix[i][j])==1:
                        d[i][j]= min(d[i-1][j],d[i][j-1],d[i-1][j-1])+1
        return max(map(max,d))**2



if __name__ == '__main__':

    t = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    print(t)
    object = Solution()
    r = object.maximalSquare(t)

    print(r)
    print('---End---')

