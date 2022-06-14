class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # Runtime: 88 ms, faster than 41.61% of Python online submissions for Reshape the Matrix.
        # Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Reshape the Matrix.
        # my own solution: time : o(m*n) space:o(m*n)
        l,m = len(nums),len(nums[0])
        if l*m!=r*c:return nums
        res=[[0]*c for _ in  range(r)]
        for i in range(l):
            for j in range(m):
                count= i*m +j
                res[int(count/c)][count%c]=nums[i][j]
        return res
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # Runtime: 85 ms, faster than 98.20% of Python3 online submissions for Reshape the Matrix.
        # Memory Usage: 14.7 MB, less than 79.01% of Python3 online submissions for Reshape the Matrix.
        # force solution: time: o(m*n) space: o(m*n)
        m, n = len(mat), len(mat[0])
        if (m == r and n == c) or m * n != r * c:
            return mat
        res = [[0] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                x, y = divmod(pos, c)
                #print('i: {} j:{} x: {} y: {} pos: {}'.format(i, j, x, y, pos))
                res[x][y] = mat[i][j]
        return res

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 = [[1,2],[3,4]]
    k1=1
    k2=4

    print('---Start---')
    print (n1)
    r = object.matrixReshape(n1,k1,k2)
    print(r)
    print('---End---')
