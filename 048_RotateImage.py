class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)== 0 or not matrix:
            return

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix)/2):
                matrix[i][j],matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1] ,matrix[i][j]

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix)-1-i):
                matrix[i][j], matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] = matrix[len(matrix) - 1 - j][len(matrix) - 1 - i], matrix[i][j]

if __name__ == '__main__':

    matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
    k = Solution()
    print 'input',matrix
    k.rotate(matrix)
    print  'result : ',matrix


