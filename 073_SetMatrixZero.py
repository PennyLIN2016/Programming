class question(object):
       def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # record if the col -0 should be set to all zero
        colZeroFlag = False
        for i in xrange(0, len(matrix)):
            if matrix[i][0] == 0:
                # before changing the matrix[i][0]
                colZeroFlag = True
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    # now the first col and row are used to record if the col/row should be set to all zero
                    matrix[i][0] = matrix[0][j] = 0


        for i in reversed(xrange(0, len(matrix))):
            for j in reversed(xrange(1, len(matrix[0]))):
                # use reversed order to make sure the matrix[i][0] / matrix[0][j] will not be changed before all other elements being changed.
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if colZeroFlag:
                matrix[i][0] = 0

if __name__ == '__main__':

    m = [
        [1,0,3],
        [1,1,3]
    ]
    t = question()
    t.setZeroes(m)
    print  'result : ',m


