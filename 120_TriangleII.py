class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in reversed(xrange (len(triangle)-1)):
            for j in xrange(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]



if __name__ == '__main__':

    inputs = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
             ]
    #inputs = [[-1],[2,3],[1,-1,-3]]

    k = Solution()
    r = k.minimumTotal(inputs)

    print r
