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