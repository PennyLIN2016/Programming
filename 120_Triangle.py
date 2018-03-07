class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)== 0:
            return 0
        s = triangle[0]*len(triangle)
        for i in xrange(1,len(triangle)):
            for j in xrange(i+1):
                if j == 0:
                    # use s[-1] to keep the s[j-1]
                    s[-1] = s[j]
                    s[j] += triangle[i][j]
                    continue
                if j == i:

                    s[j] = s[-1] +triangle[i][j]
                    continue
                tmp = s[j]
                s[j] = min(s[-1],s[j])+ triangle[i][j]
                s[-1] = tmp
        return min(s)



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
