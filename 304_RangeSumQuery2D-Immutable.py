class NumMatrix(object):
    #Runtime: 96 ms, faster than 67.02% of Python online submissions for Range Sum Query 2D - Immutable.
    #Memory Usage: 15 MB, less than 18.75% of Python online submissions for Range Sum Query 2D - Immutable.
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            m, n =0,0
        else:
            m = len(matrix)
            n= len(matrix[0])
        self.sumMatrix =[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.sumMatrix[i][j]= self.sumMatrix[i-1][j] + self.sumMatrix[i][j-1]  - self.sumMatrix[i-1][j-1] + matrix[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumMatrix[row2+1][col2+1]+self.sumMatrix[row1][col1]- self.sumMatrix[row2+1][col1]-self.sumMatrix[row1][col2+1]

if __name__ == '__main__':
    s =  [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
            ]
    print s
    obj = NumMatrix(s)
    i1,j1 = 1,1
    i2,j2 = 2,2


    r = obj.sumRegion(i1,j1,i2,j2)

    print(r)
    print('---End---')

# param_1 = obj.sumRegion(row1,col1,row2,col2)


