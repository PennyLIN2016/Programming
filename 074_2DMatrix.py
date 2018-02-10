class question(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or target is None:
            return False
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        head = 0
        tail = len(matrix)*len(matrix[0])-1

        while head<= tail:
            mid = (head+tail)/2
            raw = mid/len(matrix[0])
            col = mid%len(matrix[0])
            if matrix[raw][col] == target:
                return True
            elif matrix[raw][col]> target:
                tail = mid-1
            else:
                head= mid +1
        return False

if __name__ == '__main__':

    '''m =  [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
         ]'''
    m = []
    t = question()
    target = 0
    r = t.searchMatrix(m,target)
    print  'result : ',r


