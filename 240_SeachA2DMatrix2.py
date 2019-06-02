class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Runtime: 48 ms, faster than 94.05% of Python online submissions for Search a 2D Matrix II.
        # Memory Usage: 15.7 MB, less than 58.97% of Python online submissions for Search a 2D Matrix II.
        # to travel the matrix, make sure the pos can move forward based on the value is greater or less than the target.
        # so should start for the right top or left bottom
        # time complexity: o(n+m)
        if not matrix or not matrix[0]: return False
        row= len(matrix)
        col= len(matrix[0])
        #i ,j = 0,col-1
        i,j= row-1,0
        while i>=0 and j <col:
            # get the target
            if matrix[i][j]==target: return True
            # the top and right sides has been travelled.
            # > target, the target should be the left side
            elif  matrix[i][j]>target:
                i-=1
            # < target. the target should be the down side .
            else:
                j+=1

        return False




    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Runtime: 144 ms, faster than 27.40% of Python online submissions for Search a 2D Matrix II.
        # Memory Usage: 15.5 MB, less than 97.15% of Python online submissions for Search a 2D Matrix II.

        return any(target in row for row in matrix)

if __name__ == '__main__':
    nums = [[-5]]
    k =-5
    p = Solution()
    print(p.searchMatrix(nums,k))