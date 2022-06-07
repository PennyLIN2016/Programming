class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # Runtime: 152 ms, faster than 89.11% of Python online submissions for Brick Wall.
        # Memory Usage: 16.5 MB, less than 66.67% of Python online submissions for Brick Wall.
        # my own solution: time: o(r*c) time : o(c)
        dp = {}
        for r in range(len(wall)):
            cur=0
            for i in range(len(wall[r])-1):
                # dp[i] : the count of edge in this position
                cur+=wall[r][i]
                if cur in dp:
                    dp[cur]+=1
                else:
                    dp[cur]=1
        #print(dp)
        res=len(wall)
        for key in dp:
            res=min(res,len(wall)-dp[key])
        return res

    def leastBricks(self, wall: list[list[int]]) -> int:
        # Runtime: 190 ms, faster than 86.68% of Python3 online submissions for Brick Wall.
        # Memory Usage: 19 MB, less than 57.54% of Python3 online submissions for Brick Wall.
        # time: o(len(wall) * len(bricks)) space: 0(len(wall) * len(bricks))
        linePoints = {}
        maxPoints = 0
        for row in wall:
            endSum = 0
            for i, brick in enumerate(row):
                if i != len(row) - 1:
                    endSum += brick
                    if endSum in linePoints:
                        linePoints[endSum] += 1
                    else:
                        linePoints[endSum] = 1
                    maxPoints = max(maxPoints, linePoints[endSum])
        return len(wall) - maxPoints



if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1=[[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]


    print('---Start---')
    print (n1)
    r = object.leastBricks(n1)
    print(r)
    print('---End---')
